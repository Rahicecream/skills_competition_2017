import pyttsx3
engine=pyttsx3.init()

def rahi(text):
    engine.say(text)
    engine.runAndWait()
