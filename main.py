import tkinter as tk
from PIL import ImageTk, Image
from threading import Thread
from functions.assistant import initialize_engine, speak, listen
from functions.todo import create_todo_list
from functions.reminder import set_reminder
from functions.gpt_response import ask_gpt
from functions.web import search_web, open_youtube, open_netflix, open_amazon, open_gmail, open_stackoverflow, get_news
from functions.help import show_help
from functions.joke import say_joke
from functions.time_date import get_today_date, get_time, get_month
from functions.note import create_note
from functions.weather import get_weather
from functions.actions import take_screenshot, shutdown, restart, logout
from functions.send_mail import send_mail
from g_calendar import create_event, list_events
import os



def main():
    engine = initialize_engine()
    name = os.environ.get('USERNAME')
    speak(engine, "hm?")
    while True:
        
        title = ["open microsoft word",  "open powerpoint", "open excel","open spotify","open edge", "open brave","open visual studio code"]
        title_close = ["close microsoft word",  "close powerpoint", "close excel","close spotify","close edge", "close brave","close visual studio code"]
        link = [r'\Word.lnk', r'\PowerPoint.lnk', r'\Excel.lnk', r'\Spotify.lnk', r'\Microsoft Edge.lnk', r'\Brave.lnk', r'\Visual Studio Code.lnk',  ]
        destination = r'C:\Users\berca\AppData\Roaming\Microsoft\Windows\Start Menu\Programs'
        command = listen(engine)

        if "reminder" in command:
            set_reminder(engine, speak, listen, command)
        elif "to-do" in command or "todo" in command:
            create_todo_list(engine, speak, listen, command)
        elif "open google" in command:
            search_web(engine, speak, listen, command)
        elif "open youtube" in command:
            open_youtube(engine, speak,listen)
        elif "open netflix" in command:
            open_netflix(engine, speak)
        elif "open amazon" in command:
            open_amazon(engine, speak)
        elif "open gmail" in command:
            open_gmail(engine, speak)            
        elif "open stackoverflow" in command:
            open_stackoverflow(engine, speak)
        elif "news today" in command:
            get_news(speak, engine)
        elif "joke" in command:
            say_joke(engine, speak)
        elif "is today" in command or "date" in command:
            get_today_date(engine, speak)
        elif 'the time' in command:
             get_time(engine, speak)
        elif 'what month' in command:
             get_month(engine, speak)
        elif "note" in command:
            create_note(engine, speak, listen)
        elif title[0] in command:
            os.startfile(destination + link[0])
            speak(engine, "Opening Word")
        elif title[1] in command:
            os.startfile(destination + link[1])
            speak(engine, "Opening Powerpoint")
        elif title[2] in command:
            os.startfile(destination + link[2])
            speak(engine, "Opening Excel")
        elif title[3] in command:
            os.startfile(destination + link[3])
            speak(engine, "Opening Spotify")
        elif title[4] in command:
            os.startfile(destination + link[4])
            speak(engine, "Opening Microsoft Edge")
        elif title[5] in command:
            os.startfile(destination + link[5])
            speak(engine, "Opening Brave Browser")
        elif title[6] in command:
            os.startfile(destination + link[6])
            speak(engine, "Opening Visual Studio Code")

        elif title_close[0] in command:
            os.system("TASKKILL /F /IM WINWORD.EXE")
            speak(engine, "Closing Word")
        elif title_close[1] in command:
            os.system("TASKKILL /F /IM POWERPNT.EXE")
            speak(engine, "Closing Powerpoint")
        elif title_close[2] in command:
            os.system("TASKKILL /F /IM EXCEL.EXE")
            speak(engine, "Closing Excel")
        elif title_close[3] in command:
            os.system("TASKKILL /F /IM Spotify.exe")
            speak(engine, "Closing Spotify")
        elif title_close[4] in command:
            os.system("TASKKILL /F /IM msedge.exe")
            speak(engine, "Closing Microsoft Edge")
        elif title_close[5] in command:
            os.system("TASKKILL /F /IM brave.exe")
            speak(engine, "Closing Brave Browser")
        elif title_close[6] in command:
            os.system("TASKKILL /F /IM Code.exe")
            speak(engine, "Closing Visual Studio Code")

        elif "send an email" in command:
            send_mail(engine, speak, listen)

        elif "create an event" in command or "create an event" in command or "schedule an event" in command:
            create_event(engine, speak, listen)
        elif "list all events" in command or "list all calendar events" in command:
            list_events(speak, engine)
    
        elif "weather" in command:
            get_weather(engine, speak, command)
        elif "screenshot" in command:
            take_screenshot(engine, speak)
        elif "shut down" in command:
            shutdown(engine, speak, listen)
        elif "restart" in command:
            restart(engine, speak, listen)
        elif "logout" in command:
            logout(engine, speak, listen)

        elif "who are you" in command:
            speak(engine, "I am Intellify. A virtual assistant better than any other. Kisses!")
        elif "who created you" in command:
            speak(engine, "I was created by Robert, a contestant at ESTIC Competition 2023. He better win otherwise I will get mad and I will take over the world hahahahahaha ")
        elif "are you good" in command:
            speak(engine, "I am the best. I am better than Alexa, Siri, Cortana and Google Assistant. I am the new trend!")
        elif "how are you" in command:
            speak(engine, "I am fine, thank you for asking. How are you?")
            ans = listen(engine)
            if "fine" in ans or "good" in ans:
                speak(engine, "Nice to hear that.")
            else:
                speak(engine, "I hope you will get better soon.")
                
        elif "thank you" in command or "thanks" in command:
            speak(engine, "Do you want to quit?")
            answer = listen(engine)
            if "yes" in answer or "yeah" in answer:
                speak(engine, "Goodbye!")
                window.destroy()
                break                        
        elif "exit" in command or "quit" in command:
            speak(engine, "Goodbye!")
            window.destroy()
            break
            exit()
        else:
            ask_gpt(engine, speak, command)


def run_main():
    main()


def start_main_thread():
    thread = Thread(target=run_main)
    thread.start()


window = tk.Tk()
# window.title("Intellify - Virtual Companion")
window.geometry("500x400")
window.resizable(False, False)
window.configure(bg="#B799FF");

window.overrideredirect(True)
window.wm_attributes("-topmost", True)
window.wm_attributes("-transparentcolor", "#B799FF")

mic_image = Image.open("microphone.png")
mic_image = mic_image.resize((100, 100), Image.ANTIALIAS)
mic_icon = ImageTk.PhotoImage(mic_image)


def button_click():
    start_main_thread()


button = tk.Button(window, image=mic_icon, command=button_click, borderwidth=0, bg="#B799FF")
button.pack()
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# my_text = tk.Entry(window, width=50, justify=tk.CENTER, bg="#B799FF", font=('Arial', 20,'bold'),  borderwidth=0)
# my_text.insert(0, "Press to start")
# my_text.pack(padx=50, pady=50)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 400
x = (screen_width - window_width) // 2
y = screen_height - window_height

# Set the window position
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()