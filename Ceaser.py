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

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: \n", query)

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    Wishme()
    takeCommand()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'check my mail' in query:
            webbrowser.open("mail.google.com/mail/u/0/#inbox")

        elif 'caesar' in query:
            speak("Yes Sir")
        elif 'can you help me' in query:
            speak("Yes sir . Always happy to help you")
        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        