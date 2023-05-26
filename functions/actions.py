import pyautogui
import os


def take_screenshot(engine, speak):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('screen.png')
    speak(engine, "Screenshot saved.")


def shutdown(engine, speak, listen):
    speak(engine, "Are you sure you want to shutdown?")
    answer = listen(engine)
    if "yes" in answer or "yeah" in answer:
        speak(engine, "Shutting down.")
        os.system("shutdown /s /t 1")
    else:
        speak(engine, "Shutdown cancelled.")


def restart(engine, speak, listen):
    speak(engine, "Are you sure you want to restart?")
    answer = listen(engine)
    if "yes" in answer or "yeah" in answer:
        speak(engine, "Restarting.")
        os.system("shutdown /r /t 1")
    else:
        speak(engine, "Restart cancelled.")

def logout(engine, speak, listen):
    speak(engine, "Are you sure you want to logout?")
    answer = listen(engine)
    if "yes" in answer or "yeah" in answer:
        speak(engine, "Logging out.")
        os.system("shutdown -l")
    else:
        speak(engine, "Logout cancelled.")