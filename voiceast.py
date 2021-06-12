import pyttsx3
import datetime

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
    
    speak("Hi, I am Helex. PLease tell me how can I help you")
if __name__ == '__main__':
    wishme()