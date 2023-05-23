import os
import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3

def initialize_engine():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 180)     
    return engine

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
    except Exception as e:
        print("Sorry, I didn't understand that. Can you please repeat?")
        return "None"

    return command.lower()