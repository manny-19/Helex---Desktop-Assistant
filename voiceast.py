import pyttsx3           # -m venv PATH OF FOLDER\venv  
import datetime                  # use this to create virtual env if error in importing libraries
import speech_recognition as sr
engine  = pyttsx3.init('sapi5') # sapi5 is microsoft speech API , to use inbuilt voices
voices = engine.getProperty('voices')
#print(voices)         
engine.setProperty('voice', voices[1].id)    #[1] == female voice, [0] == male voice

def speak(audio):      #speak function inputs string
    engine.say(audio)  
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour) 
    
    if(hour>=0 and hour<12):
        speak("Good Morning!")  
         
    elif(hour>=12 and hour<16):
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")    
    
    speak("Hey, I am Helex. PLease tell me how can I help you")
    
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
    
if __name__ == '__main__':
    wishme()
    takeCommand()