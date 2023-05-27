from datetime import datetime, timedelta
import utils.calendar_setup as calendar_setup


def create_event(engine, speak, listen):
   # creates one hour event tomorrow 10 AM IST
   service = calendar_setup.get_calendar_service()

   speak(engine, "What is the title of the event?")
   title = listen(engine)

   speak(engine, "Do you want to add a description?")
   ans = listen(engine)
   if "yes" in ans or "yeah" in ans:
        speak(engine, "What is the description of the event?")
        description = listen(engine)
   else:
        description = ""

   speak(engine, "What is the start date of the event?")
   date1 = listen(engine)
   date_format = "%B %dth %Y %I%p"
   date1 = datetime.strptime(date1, date_format)

   speak(engine, "What is the end date of the event?")
   date2 = listen(engine)
   date_format = "%B %dth %Y %I%p"
   date2 = datetime.strptime(date2, date_format)
   
   start = date1.isoformat()
   end = date2.isoformat()

   print(start)
   print(end)

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": title,
           "description": description,
           "start": {"dateTime": start, "timeZone": 'Europe/Bucharest'},
           "end": {"dateTime": end, "timeZone": 'Europe/Bucharest'},
       }
   ).execute()

   speak(engine, "Event created successfully")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])


def list_events(speak, engine):
   service = calendar_setup.get_calendar_service()
   now = datetime.utcnow().isoformat() + 'Z' 
   events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=10, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   speak(engine, "Upcoming events:")
   if not events:
       speak(engine, 'No upcoming events found.')
   for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
       start_date = datetime.strptime(start[:19], "%Y-%m-%dT%H:%M:%S")
       speak(engine, f"{event['summary']} on {start_date}")
