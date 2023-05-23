from functions.assistant import initialize_engine, speak, listen
from functions.todo import create_todo_list
from functions.reminder import set_reminder
from functions.gpt_response import ask_gpt
from functions.web import search_web, open_youtube
from functions.help import show_help
from functions.joke import say_joke
import os


def main():
    engine = initialize_engine()
    name = os.environ.get('USERNAME')
    speak(engine, f"Hello, {name}. I am Intellify. How can I help you today?")
    
    while True:
        command = listen()
        
        if "reminder" in command:
            set_reminder(engine, speak, listen, command)
        elif "to-do" in command or "todo" in command:
            create_todo_list(engine, speak, listen, command)
        elif "search" in command:
            search_web(engine, speak, command)
        elif "youtube" in command:
            open_youtube(engine, speak)
        elif "help" in command:
            show_help(engine, speak)
        elif "question" in command:
            ask_gpt(engine, speak, listen, command)
        elif "joke" in command:
            say_joke(engine, speak);
        elif "thank you" in command or "thanks" in command or "exit" in command or "quit" in command:
            speak(engine, "Goodbye!")
            break

if __name__ == "__main__":
    main()
