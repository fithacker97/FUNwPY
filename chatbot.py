import google.generativeai as genai

API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)
MODEL = genai.generative_models.get("gemini-2.0-flash")

chat = MODEL.start_chat()

response = chat.send_message(
    "Write a poem about a lonely computer in the style of Shakespeare." 
)   

print("Gemini response:", response.text)