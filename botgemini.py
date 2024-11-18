import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyAQuW_uiHzXNmwpJ8rNu_V8eWsPminLND4')

model = genai.GenerativeModel("gemini-1.5-flash")
while True:
    request = input("Type here: ")
    if request == 'exit' :
        break
    response = model.generate_content(request)
    print(response.text)