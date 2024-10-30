import google.generativeai as genai


def get_response(api_key, prompt):
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return (response.text)