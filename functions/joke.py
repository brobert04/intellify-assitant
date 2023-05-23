import pyjokes


def say_joke(engine, speak):
    speak(engine, "Let me think of one...");
    joke = pyjokes.get_joke()
    speak(engine, joke)