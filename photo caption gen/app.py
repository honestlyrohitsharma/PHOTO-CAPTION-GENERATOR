# app.py

import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import os
from dotenv import load_dotenv
import google.generativeai as genai 


load_dotenv()

# --- Page Configuration ---
st.set_page_config(
    page_title="Memory Caption Generator",
    page_icon="📸",
    layout="centered",
)

@st.cache_resource
def load_models():
    """Loads the BLIP image captioning model and processor from Hugging Face."""
    try:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
        return processor, model
    except Exception as e:
        st.error(f"Failed to load the image model. Please check your connection. Error: {e}")
        return None, None


def get_image_description(image, processor, model):
    """Generates a descriptive caption for an image using the BLIP model."""
    try:
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs, max_new_tokens=50)
        description = processor.decode(out[0], skip_special_tokens=True)
        return description
    except Exception as e:
        st.error(f"Error during image description: {e}")
        return "Could not describe the image."

def generate_personalized_caption(image_desc, memory, gemini_model): 
    """Generates a personalized caption using Gemini based on image description and user memory."""
    try:
        prompt = f"""
        You are a creative photo caption writer for social media.
        Your task is to combine a factual description of an image with a user's personal memory to create a short, engaging, and heartfelt caption.

        Factual Image Description: "{image_desc}"
        User's Personal Memory: "{memory}"

        Based on both pieces of information, write a perfect caption. Make it sound natural and personal. It's for an Indian user, so feel free to use culturally relevant nuances if appropriate, but keep it universal.
        """
       
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error connecting to Gemini API: {e}")
        return "Failed to generate caption."


st.title("📸 Photo Caption Generator with Memory")
st.markdown("Powered by Google Gemini & BLIP")


processor, model = load_models()


api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API key is not found! Please add it to your .env file.")
    st.stop()

genai.configure(api_key=api_key)
gemini_model = genai.GenerativeModel('gemini-1.5-flash') 


uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])
user_memory = st.text_input("Add a personal memory (e.g., 'Diwali in Delhi 2024')", "My favourite moment.")

if uploaded_file is not None and model is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Your Uploaded Photo", use_column_width=True)

    if st.button("✨ Generate Caption"):
        with st.spinner("Analysing your photo and crafting the perfect caption..."):
            image_desc = get_image_description(image, processor, model)
            final_caption = generate_personalized_caption(image_desc, user_memory, gemini_model)

            st.subheader("Your Personalized Caption:")
            st.info(final_caption)

            with st.expander("See the AI's initial observation"):
                st.write(f"**Raw Description:** {image_desc}")
else:
    if model is None:
        st.warning("The image processing model could not be loaded. The app is not functional.")