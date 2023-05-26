import requests

def get_weather(engine, speak, command):
    char_remov = ["how", "is", "weather", "in", "what", "the", "temperature", "of", "city", "is", "it", "today", "like", "in", "degrees"]
    try:
        for char in char_remov:
            command = command.replace(char, "")
        city = command
        api = "http://api.openweathermap.org/data/2.5/weather?q=" +city+"&appid=c218644828c9a78f7a1be0c1ea78a416" 
        response = requests.get(api).json()
        temp_max = int(response['main']['temp_max'] - 273.15)
        temp_min = int(response['main']['temp_min'] - 273.15)
        feels_like = int(response['main']['feels_like'] - 273.15)
        description = response['weather'][0]['description']
        speak(engine, f"The weather in  in {city} is {description}. The maximum temperature is {temp_max} degrees celsius and the minimum temperature is {temp_min} degrees celsius. Right now it feels like {feels_like} degrees celsius.")

        return None
    except:
        speak(engine, "Sorry, I couldn't understand the city you provided. Please try again.") 