import webbrowser

def search_web(engine, speak, command):
    search_terms = command.replace("search", "").strip()
    if search_terms:
        url = f"https://www.google.com/search?q={search_terms}"
        speak(engine, f"Searching for '{search_terms}'")
        webbrowser.open(url)
    else:
        speak(engine, "Please provide a search term.")



def open_youtube(engine, speak):
    url = "https://www.youtube.com"
    speak(engine, "Opening YouTube")
    webbrowser.open(url)