import os
import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3

def initialize_engine():
    engine = pyttsx3.init('sapi5')
    # rate = engine.getProperty('rate')   
    # engine.setProperty('rate', 150)   
    voices = engine.getProperty('voices')      
    engine.setProperty('voice', voices[1].id)  
    return engine

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()


def listen(engine):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
    except Exception as e:
        speak(engine, "Sorry, I didn't understand that")
        return listen(engine)

    return command.lower()