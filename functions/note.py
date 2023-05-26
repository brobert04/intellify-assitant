import subprocess

def create_note(engine, speak, listen):
    speak(engine, "How should I name the note?")
    name = listen(engine);
    speak(engine, "What should the note contain?")
    content = listen(engine)
    file_name = name + ".txt"
    with open(file_name, "w") as f:
        f.write(content)
    subprocess.Popen(["notepad.exe", file_name])   
    