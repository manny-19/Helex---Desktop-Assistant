import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
from googlesearch import search
import webbrowser as wb 
import os
from PyDictionary import PyDictionary

wb.register('chrome',None)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Helex. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            print('Searchinng Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'on google' in query:
            speak('searching on google')
            print("Searching on Google...")
            query = query.replace("on google","")
            for j in search(query, tld="co.in", num=1, stop=10, pause=2):
                wb.register('chrome',None)
                wb.open(j)
                break
                
        elif 'open youtube' in query:
            speak('Opening Youtube')
            wb.register('chrome',None)
            wb.open('youtube.com')
            
        elif 'open google' in query:
            speak('Opening google')
            wb.register('chrome',None)
            wb.open('google.com')
            
        elif 'the time' in  query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")
        
        elif 'open visual studio code' in query:
            speak('Opening V S Code')
            code_path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
        elif 'meaning of' in query:
            speak('according to google')
            query = query.replace('meaning of',"")
            for j in search(query, tld="co.in", num=1, stop=10, pause=2):
                wb.register('chrome',None)
                wb.open(j)
                break
            