

def show_help(engine, speak):
    help_text = """
    I can help you with the following tasks:
    1. Set reminders: Say 'set reminder' followed by the reminder and time.
    2. Create to-do lists: Say 'create to-do list' and then list your tasks one by one.
    3. Search the web: Say 'search' followed by the search terms.
    4. Open YouTube. Say Open YouTube.
    4. Show available commands: Say 'help'.
    And much more... just ask and see!
    To exit, say 'exit' or 'quit'.
    """
    print(help_text)
    speak(engine, help_text)