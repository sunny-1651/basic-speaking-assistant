import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#you can change voice according to your preference instead of 1 you can try 0, 1, 2... depending on number of voices installed in your system
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning")
        speak("suprabhat")

    elif hour>=12 and hour<16:
        speak("Good Afternoon")
        speak("namaste")

    elif hour>=16 and hour<19:
        speak("Good Evening")
        speak("susandhya")
    else:
        speak("namaste")


def takeCommand():
    
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
        print("I was unable to transcribe that, Could you repeat it please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=20)
            speak("According to Wikipedia")
            print("According to Wikipedia", results)
            speak(results)
        #this is my college portal you can change the query according to your preference
        elif query == "open vtop" or query == "open vtop portal":
            # insert the url of website you intend to open
            webbrowser.open("https://vtop.vit.ac.in/vtop/initialProcess")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google ' in query:
            query = query.replace("google ", "")
            opnt(url)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chrome' or 'open browser' in query:
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chromepath)
        
        elif 'play music' or 'spotify' or 'play spotted' in query:
            spotifyPath = "C:\\Users\\SUNNY\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
            os.startfile(spotifyPath)

        elif 'offline music' or "saved music" in query:
            music_dir = "C:\\Users\\SUNNY\\Music\\Playlists\\all_songs_A-Z.zpl"
            os.startfile(music_dir)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"it is {strTime} according to my clock")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm 2020.2.2\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'stop listening' in query:
            break

        elif 'close my assistant' in query:
            speak("it was nice helping you sir")
            hour = int(datetime.datetime.now().hour)
            if hour>18 and hour<6:
                speak("good night")
                speak("shubh ratri")
            else:
                speak("have a good day")
                speak("aapka din shubh ho")
            print('bye')

        exit()

