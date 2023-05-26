import datetime

def get_today_date(engine, speak):
    dateT = datetime.date.today()
    today = dateT.strftime("%B %d, %Y")
    speak(engine, today);

def get_month(engine, speak):
    dateT = datetime.date.today()
    month = dateT.strftime("%B")
    speak(engine, month);


def get_time(engine, speak):
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(engine,f"The time is {strTime}")
