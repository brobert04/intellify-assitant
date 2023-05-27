import os
import openai

openai.api_key = "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"

def ask_gpt(engine, speak, command):
    speak(engine, "Let me think about that.")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=command,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    speak(engine, response.choices[0].text)