import pyttsx3
import datetime
import os
import speech_recognition as sr 
import pyaudio
import webbrowser
import wikipedia




my_assistants = 'Diva'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
print(voices[2])
engine.setProperty('voice',voices[2])

def talk(audio):
    engine.say(audio)
    engine.runAndWait()
talk("Hello Sir!")

def wish_audience():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Good Morning")
    elif hour>12 and hour <2:
        talk("Good Afternooon ")
    else :
        talk("Good Evening ")

    talk(f"I am {my_assistents}. I can help you with a variety of tasks like searching the web, opening apps, playing music, providing information from Wikipedia, and much more.")
    talk(" Just tell me what you need, and I'll do my best to assist you!")

def get_audio():
    r = sr. Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    try :
        print("I am recognizing you........")
        query = r.recognize_google(audio,language = 'en-in')
        print("You said :" , query)
    except Exception :
        print("Sorry, I am not able to understand your voice. Please try again.")
        return None
    return query




if __name__ == '__main__':

    wish_audience()
    while True:
       query = get_audio()

       if query is not None:
          query = query.lower()
          if 'wikipedia' in query:
              query = query.replace('wikipedia','')
              talk(f"Searching Wikipedia for {query}")
              result =wikipedia.summary(query,sentences = 2 )
              talk(f"according to the wikipedia {result} ")
            
              print(result)
          elif 'open youtube' in query:
              talk("Opening Youtube")
              webbrowser.open('www.youtube.com')
          elif 'open google' in query:
              talk("Opening Google")
              webbrowser.open('www.google.com')
          elif 'open instagram' in query:
              talk("Opening Instagram")
              webbrowser.open('www.instagram.com')
          elif 'open java project' in query:
              talk("opening your java project")
              os.startfile("C:\\Users\\Adarsh\\OneDrive\\Desktop\\java project")
          elif 'open Cmd' in query:
              talk("Opening Command Prompt")
              os.system('start cmd')  
          elif 'open your image' in query:
              talk("Opening my image")
              os.startfile("C:\\Users\\Adarsh\\OneDrive\\Desktop\\srk.webp")
          elif 'exit' in query:
              talk("Goodbye, My Dear. Have a great day!")
              break
          else:
             search = 'https://www.google.com/search?q='+ query
             webbrowser.open(search)
       else:
            talk("I didn't catch that. Could you please repeat?")


