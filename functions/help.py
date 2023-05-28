

def show_help(engine, speak):
    help_text = """
    I can do the following tasks:
    Create to-do lists
    Search the web
    Open YouTube or other websites
    Open application from your computer & close them
    Control your system by voice
    Send emails
    Schedule events in calendar
    And much more... just ask and see!
    To exit, say 'exit' or 'quit'.
    """
    print(help_text)
    speak(engine, help_text)