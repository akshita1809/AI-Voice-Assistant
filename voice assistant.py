
import pyttsx3 #pip install pyttsx3
import datetime #importing date and time libraries

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)
#print('property set')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#print('audio running')

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak('the time is')
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('the date today is')
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak('welcome back!')
   
    hour = datetime.datetime.now().hour

    if hour>= 0 and hour<= 11:
        speak('good morning')
    elif hour>= 12 and hour<= 16:
        speak('good afternoon')
    elif hour>= 17 and hour<=23:
        speak('good evening')
    else:
        speak('good night')

 
def dateandtime():
    date()
    time()


speak('Hi Akshita!') #print('speaking')

wishme()

speak('How may i help you?')
