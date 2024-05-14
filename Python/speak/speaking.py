import pyttsx3
import datetime 
import sys 
import speech_recognition as sr
sys.path.append("E:\\Code\\Python\\Doanreal")
from Arduino.door import *
from Arduino.led import *
from pyfirmata import *

friday=pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id) 

board =Arduino ("COM9")
    
maindor=door('8','9','3','5',board)
led13 =LED ("13",board)

        
def speak(audio):
    print('F.R.I.D.A.Y: ' + audio)
    friday.say(audio)
    friday.runAndWait()
   
    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p") 
    speak("It is")
    speak(Time)

def welcome():
        #Chao hoi
        hour=datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            speak("Good Morning Sir!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon Sir!")
        elif hour>=18 and hour<24:
            speak("Good Evening sir")
        speak("How can I help you,boss") 


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.adjust_for_ambient_noise(source, duration=2)
        audio = c.listen(source, timeout=3)
    try:
        query = c.recognize_google(audio,language='en-US')
        print("chotrannam: "+query)
    except sr.UnknownValueError:
        print('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Your order is: '))
    return query

def Assigment():
    welcome()

    while True:
        query=command().lower()
        if "turn on" in query:
            led13.turnOn()
            speak("the light is on")
        elif "turn off " in query:
            led13.turnOff()
            speak("the light is off")
        elif "open " in query:
            maindor.mocua()
            speak ("door is open")
        elif "close" in query:
            maindor.dongcua()

        elif "quit" in query:
            speak("Friday is off. Goodbye boss")
            quit()