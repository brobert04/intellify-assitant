import datetime

def set_reminder(engine, speak, listen, command):
    speak(engine, "What should I remind you about?")
    reminder = listen()
    if "exit" in reminder or "quit" or "mistake" or "back" in reminder:
        speak(engine, "Alright, I will not set a reminder.")
        return
    speak(engine, "When do you want to be reminded? Please say the time in hours and minutes.")
    reminder_time = listen()
    try:
        hour, minute = map(int, reminder_time.split())
        now = datetime.datetime.now()
        reminder_datetime = now.replace(hour=hour, minute=minute)
        if now > reminder_datetime:
            reminder_datetime += datetime.timedelta(days=1)
        speak(engine, f"Alright, I will remind you about '{reminder}' at {hour:02d}:{minute:02d}.")
        while True:
            if datetime.datetime.now() >= reminder_datetime:
                speak(engine, f"Reminder: {reminder}")
                break
    except ValueError:
        speak(engine, "Sorry, I couldn't understand the time you provided. Please try again.")
