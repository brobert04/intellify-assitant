import webbrowser
import bs4
import urllib.request

def search_web(engine, speak, command):
    search_terms = command.replace("search", "").strip()
    if search_terms:
        url = f"https://www.google.com/search?q={search_terms}"
        speak(engine, f"Searching for '{search_terms}'")
        webbrowser.open(url)
    else:
        speak(engine, "Please provide a search term.")


def open_youtube(engine, speak, listen):
    speak(engine, "Do you want to search for something?")
    answer = listen(engine)
    if "yes" in answer or "yeah" in answer:
        speak(engine, "What do you want to search for?")
        search_terms = listen(engine)
        url = f"https://www.youtube.com/results?search_query={search_terms}"
        speak(engine, f"Searching for '{search_terms}' on YouTube")
        webbrowser.open(url)
    else:
        url = "https://www.youtube.com"
        speak(engine, "Opening YouTube")
        webbrowser.open(url)

def open_netflix(engine, speak):
    url = "https://www.netflix.com"
    speak(engine, "Opening Netflix")
    webbrowser.open(url)

def open_amazon(engine, speak):
    url = "https://www.amazon.com"
    speak(engine, "Opening Amazon")
    webbrowser.open(url)

def open_gmail(engine, speak):
    url = "https://www.gmail.com"
    speak(engine, "Opening Gmail")
    webbrowser.open(url)

def open_stackoverflow(engine, speak):
    url = "https://www.stackoverflow.com"
    speak(engine, "Opening Stack Overflow")
    webbrowser.open(url)

def get_news(speak, engine):
    url = "https://news.google.com/news/rss"
    client = urllib.request.urlopen(url)
    xml_page = client.read()
    client.close()
    page = bs4.BeautifulSoup(xml_page, 'lxml')
    news_list = page.findAll("item")
    speak(engine, "Today's top headlines are--")
    try:
        count = 0
        for news in news_list:
            if count < 5:
                speak(engine, f"{news.title.text}")
                print()
                count+=1
            else:
                break
    except Exception as e:
        pass