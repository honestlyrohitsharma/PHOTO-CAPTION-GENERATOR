# 📸 Photo Caption Generator with Memory

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://photo-caption-generator-ufrt2zmmfcalamdgavjuik.streamlit.app/)

An AI-powered web application that generates **personalized captions for photos** by combining:
- **Factual descriptions** from BLIP (Salesforce Vision-Language model)
- **Creative captions** generated with Google Gemini API
- **User-provided memories** for a personal touch ✨

---

## 🚀 Live App
👉 Try it here: [Photo Caption Generator](https://photo-caption-generator-ufrt2zmmfcalamdgavjuik.streamlit.app/)

---

## 🖼️ Features
- Upload any photo (JPG, JPEG, PNG)
- AI generates a **raw factual description**
- Combine with your **personal memory**
- Get a short, **engaging, and heartfelt caption** suitable for social media
- Built with **Streamlit** for an interactive web experience

---

## 🛠️ Tech Stack
- **Frontend / Web App**: [Streamlit](https://streamlit.io/)
- **Image Captioning**: [BLIP model](https://huggingface.co/Salesforce/blip-image-captioning-base)  
  *(recommended for lightweight deployments)*  
- **Generative AI**: [Google Gemini API](https://ai.google.dev/)
- **Backend**: Python, Torch, Pillow
- **Deployment**: [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📂 File Structure
```bash
photo_caption_generator/
│── app.py                  # Main Streamlit app
│── requirements.txt        # Dependencies
│── README.md               # Project documentation
│── Internship-Report/      
│    └── Internship Report for project_ROHIT.pdf
│── .gitignore              # Ignore secrets like .env
