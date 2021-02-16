import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=6 and hour <12:
        speak("Hello Good morning Sir. What I can do for u?")
    elif hour >=12 and hour <18:
        speak("Hello Good Afternoon Sir. What I can do for u?")
    else:
        speak("Hello Good Evening Sir. What I can do for u?")

speak("Hi I am Caesar")