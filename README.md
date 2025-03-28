# 💬 Emotion-Aware AI Chatbot

A simple and emotionally intelligent chatbot that detects your feelings and responds accordingly using Gemini 1.5 Pro and a Hugging Face emotion model.

## ✨ Features

- Detects emotions from user input (e.g., sadness, joy, anger)
- Gemini 1.5 Pro generates emotionally aware responses
- Typing animation for a human-like feel
- Minimal, focused Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- Google Generative AI (`google-generativeai`)
- Gemini 1.5 Pro model


## 🧠 How It Works (Workflow Overview)

1. **User enters a message**  
   The chatbot interface takes the user's message using a simple text input.

2. **Emotion is detected**  
   The system uses a pre-trained emotion model to identify the underlying feeling (e.g., joy, sadness, anger).

3. **Tone-aware response is generated**  
   Based on the detected emotion, a prompt is sent to Gemini 1.5 Pro to generate a reply that fits the tone.

4. **Response is displayed with typing effect**  
   The chatbot simulates typing to make the interaction feel more human and natural.

5. **Minimalist UI with Streamlit**  
   The interface was kept clean and focused to allow for easy testing and demo usage.

## 🚀 Getting Started

To run the chatbot locally on your machine:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 Live Demo

Experience it instantly online:  
👉 [**Click here to try the chatbot!**](https://emotional-ai-chatbot-ufii8znewhxwz7zapeju7q.streamlit.app/)
