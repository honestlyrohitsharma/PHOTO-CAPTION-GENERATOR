import streamlit as st
from PIL import Image
import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- Load environment variables ---
load_dotenv()

# --- Page Configuration ---
st.set_page_config(
    page_title="Memory Caption Generator",
    page_icon="📸",
    layout="centered",
)

# --- Setup Gemini API ---
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Missing GOOGLE_API_KEY in .env or environment variables.")
    st.stop()

genai.configure(api_key=api_key)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")  # Fast multimodal model

# --- Helper Function ---
def generate_caption(image, memory, model):
    try:
        prompt = (
            "You are a creative photo caption writer. Combine the image details "
            "with the user's memory to craft a short, personalized, and heartfelt caption."
            f"\nUser's Memory: \"{memory}\""
        )
        response = model.generate_content([prompt, image])
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating caption: {e}")
        return "Failed to generate caption."

# --- Streamlit UI ---
st.title("📸 Photo Caption Generator with Memory")
st.markdown("Powered by **Google Gemini 2.5 Flash** ✨")

uploaded = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
memory = st.text_input("Add a personal memory (e.g., 'Diwali in Delhi 2024')", "")

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded Photo", use_column_width=True)

    if st.button("✨ Generate Caption"):
        with st.spinner("Crafting your caption..."):
            caption = generate_caption(img, memory, gemini_model)
            st.subheader("Your Personalized Caption:")
            st.info(caption)

# --- Footer ---
st.markdown(
    """
    <hr style="margin-top:50px;margin-bottom:10px">
    <div style="text-align:center; font-size:14px; color:gray;">
        Created by:<br>
        <b>Saptarishi Mukerjee</b> (<a href="mailto:mukherjeesaptarshi289@gmail.com">mukherjeesaptarshi289@gmail.com</a>)<br>
        <b>Shreya Ranjan</b> (<a href="mailto:shreyaranjan9431@gmail.com">shreyaranjan9431@gmail.com</a>)<br>
        <b>Rohit Sharma</b> (<a href="mailto:rohitrnps@gmail.com">rohitrnps@gmail.com</a>)
    </div>
    """,
    unsafe_allow_html=True
)
