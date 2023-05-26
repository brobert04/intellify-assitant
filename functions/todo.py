
def create_todo_list(engine, speak, listen, command):
    todo_list = []
    speak(engine, "Let's create a to-do list. Please say the tasks one by one. Say 'done' when you're finished.")
    while True:
        task = listen(engine)
        if task == "done":
            break
        todo_list.append(task)
        speak(engine, f"Added: {task}")
    speak(engine, "Here's your to-do list:")
    for task in todo_list:
        speak(engine, task)