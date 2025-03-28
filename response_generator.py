import google.generativeai as genai

genai.configure(api_key="AIzaSyBvnnAjfZmooOu6613wzX2GvapnMajMBGw")

model = genai.GenerativeModel("gemini-1.5-pro-latest")

def generate_dynamic_response(user_input, emotion):
    prompt = (
        f"The user is feeling {emotion}. "
        f"They said: '{user_input}'. "
        f"Respond like a helpful, emotionally intelligent assistant."
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating response: {e}"

