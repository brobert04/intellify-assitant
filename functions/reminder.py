import datetime

def set_reminder(engine, speak, listen, command):
    speak(engine, "Say the datetime")
    date = listen(engine)
    date_format = "%B %dth %Y %I%p"
    date = datetime.datetime.strptime(date, date_format)
    print(date.isoformat())




