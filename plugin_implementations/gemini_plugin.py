import textwrap
import google.generativeai as genai

# This is the key generated from gemini google AI studio 
# Link: https://aistudio.google.com/app/apikey
google_api_key = "[Put your API Key here]"

# Configure API key for Google Generative AI
genai.configure(api_key=google_api_key)

def to_plain_text(text):
    # Split the text into lines and process each line
    lines = text.split('\n')
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith('*'):
            line = '- ' + line[1:].strip()
        formatted_lines.append(line)
    # Join the processed lines back into a single string
    return '\n'.join(formatted_lines)

model = genai.GenerativeModel('gemini-1.5-flash')

x = input("What's your mood? \n")

question = f"Tell them on mood what could help in a list, how to improve it, their mood is {x}"

response = model.generate_content(f"{question}")

print(f"Response from generative AI:\n\n{to_plain_text(response.text)}")
