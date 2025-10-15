import google.generativeai as genai

API_KEY = "AIzaSyCvnsxyM7yefjnFOGJpHkFZQXB7BHzpo20"
genai.configure(api_key=API_KEY)
MODEL = genai.GenerativeModel("gemini-2.0-flash")

chat = MODEL.start_chat()

response = chat.send_message(
    "Write a poem about a lonely computer in the style of Shakespeare." 
)   

print("Gemini response:", response.text)
