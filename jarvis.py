import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice', voices[1].id)
#print('property set')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening!")

#print('audio running')

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('the date today is')
    speak(day)
    speak(month)
    speak(year)

speak('hello Akshita')
wishMe()
date()