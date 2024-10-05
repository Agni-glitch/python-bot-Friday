import speech_recognition as sr
import webbrowser 
import pyttsx3
import search
import requests
import genai
#you can also use gtts as text to speech reply
#you can also use pocketsphinx as speech recognizer

def getNews():
    url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=0175f2ba50344b36b523c7b00ccf4101')
    response = requests.get(url)
    return response.json()

recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def say():
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5,phrase_time_limit=1.5)
    word=r.recognize_google(audio)
    return word

def commandProcessed(c):
    print(c)
    i = c.lower()
    if i in search.objects.keys():
        speak(f'opening {i.split(' ')[-1]}')
        webbrowser.open(search.objects[i])
    elif i in search.songs.keys():
        speak(f'playing {i}')
        webbrowser.open(search.songs[i])
    elif i=='news':
        a=getNews()
        for i in range(5):
            speak(a['articles'][i]['title'])
    else:
        a= genai.res(i)
        speak(a)

if __name__ == "__main__":
    speak("Friday is active now...")
    while True:
        r = sr.Recognizer()
        try:
            print("Say something!")
            word=say()
            print(word)
            if(word.lower()=='friday'):
                speak('Sir, How can I help you')
                print("give your command")
                command=say()
                commandProcessed(command)
            elif(word.lower()=='please stop'):
                speak('goodbye sir')
                break
        except Exception as e:
            print(f"Error: {e}")