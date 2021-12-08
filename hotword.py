import os
import speech_recognition as sr

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except:
            return "None"

        return query

def WakeUp():
    while True:

        query = takecommand().lower()

        if 'wake up' in query:
            os.startfile('Main.py')

        else:
            print("Napping......")