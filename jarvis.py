
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
import os

import pafy
import vlc 
import random
  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning RAJ!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")       

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
        # speak(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Sorry my friend. I am not able to catch you")
        speak("Repeat it again") 
        print("Say that again please...")
         
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
  
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube")
             
            webbrowser.get('firefox').open("youtube.com")
            
        elif 'search' in query:
            searchin = ("https://www.google.com/search?client=firefox-b-d&q=")+query[7:]
            speak("searching")
            
            webbrowser.open(searchin)

        elif 'open google' in query:
            speak("Opening Google")
            
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("Opening StackOverflow")
            
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            speak("Playing music")
            music_urls = [
                "https://www.youtube.com/watch?v=A_z5g0_hJN8&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=2",
                "https://www.youtube.com/watch?v=qP8e7lFdEho&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=3",
                "https://www.youtube.com/watch?v=N_iW0VC3IdI&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=4",
                "https://www.youtube.com/watch?v=vbApNvaaYbc&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=5",
                "https://www.youtube.com/watch?v=nngwP1WWva4&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=6",
                "https://www.youtube.com/watch?v=MmvpbLdaIRs&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=7",
                "https://www.youtube.com/watch?v=VpJDmKKz3yg&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=8",
                "https://www.youtube.com/watch?v=93Y_eCwdR5k&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=9",
                "https://www.youtube.com/watch?v=fWajtP80g54&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=10",
                "https://www.youtube.com/watch?v=lPg2iuMAdLc&list=PL_DaWb6RFQc38S2isSKehrk0Fvktk2oNp&index=12"
            ]
            random_url = random.choice(music_urls)
            webbrowser.open(random_url)
        elif 'stop' in query:
            webbrowser.open("https://www.youtube.com/")
            

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")



        elif 'mail ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rajkisanssvrs@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
        elif 'hi jarvis' in query:
            speak("Hi How are you?")
        elif 'fine' in query:
            speak("I am Fine, How may I help you?")
