import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def ask_gpt(engine, speak, listen, command):
    speak(engine, "What would you like to ask?")
    question = listen()
    speak(engine, "Let me think about that.")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    speak(engine, response.choices[0].text)