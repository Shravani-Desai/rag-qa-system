import google.generativeai as genai

genai.configure(api_key="AIzaSyBZ6oTNOFiJ8x2jP24Nw3i2WGftn5vAGcs")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)