import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "Remon"
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

def speak(pyaudio):
    engine.say(pyaudio)
    engine.runAndWait()
# This function will wish you
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)



    #speak(" How may i help you ?")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said; { query}\n")

    except Exception as e:
        print("Say that again please")

        query = None
        return query





speak("Initializing Jarvis....")
wishMe()
query = takeCommand()

if 'wikipedia' in query.lower():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "" )
    results = wikipedia.summary(query,sentence = 2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")