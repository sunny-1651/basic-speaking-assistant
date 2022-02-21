import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import random
import time
import os
import re
import psutil

engine = pyttsx3.init()
newVoiceRate = 115
engine.setProperty('rate',newVoiceRate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[51].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    sal = ["hey", "hey buddy", "hey budd,", "hi", "hello", "hello, how are you", "howdy", "howdy, mate"]
    speak(random.choice(sal))
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")

    elif hour >= 16 and hour < 19:
        speak("Good Evening")

    speak("My name is scooby, and i am up and running")


def takeCommand(x = "Listening..."):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(x)
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        print("I was unable to transcribe that, Could you repeat it please")
        return "None"
    return query




if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "scooby" in query:
            query = query.replace("scooby ", "")
            if "volume to" in query:
                x = re.findall(r'\d+', query)
                os.system(f"amixer set Master {x[0]}%")
            #     os.system(f"amixer set Headphone {x[0]}%")
            #     os.system(f"amixer set Headset {x[0]}%")

            elif "music" or "song" or "tune" in query:
                if "pause" in query:
                    os.system(
                        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause")
                elif "play" in query:
                    os.system(
                        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play")
                elif "next" in query:
                    os.system(
                        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")
                elif "previous" in query:
                    os.system(
                        "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")

            elif "open my downloads" in query:
                os.system("xdg-open ~/Downloads")

            elif "open my documents" in query:
                os.system("xdg-open ~/Documents")

            elif "open my pictures" in query:
                os.system("xdg-open ~/Pictures")

            elif 'wikipedia' in query:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query)
                x = wikipedia.page(query)
                print("\n\n.....................................\n", x.url, "\n.....................................\n")
                speak("According to Wikipedia")
                print("According to Wikipedia: ", results)
                speak(results)
            # this is my college portal you can change the query according to your preference
            elif query == "open vtop" or query == "open vtop portal":
                query = f'brave-browser-stable "https://vtop.vit.ac.in/vtop/initialProcess"'
                os.system(f"gnome-terminal -e {query}")
                speak("opening vtop")

            elif 'open youtube' in query:
                query = f'firefox "youtube.com"'
                os.system(f"gnome-terminal -e {query}")
                speak("opening youtube")

            elif 'google ' in query:
                query = query.replace("google ", "")
                query = query.replace(" ", "+")
                query = f'brave-browser-stable "https://www.google.com/search?channel=fs&client=ubuntu&q={query}"'
                os.system(f"gnome-terminal -e {query}")
                speak("googling")

            elif 'open brave' in query or 'open browser' in query:
                chromepath = "/usr/bin/brave-browser-stable"
                speak("opening browser, brave ")
                print("opening browser, brave ")
                os.system(f"gnome-terminal -e {chromepath}")

            elif 'open edge' in query:
                chromepath = "/usr/bin/microsoft-edge-stable"
                speak("opening edge")
                print("opening edge")
                os.system(f"gnome-terminal -e {chromepath}")

            elif 'open college mail' in query:
                query = 'microsoft-edge-stable "https://mail.google.com/mail/u/0/#inbox"'
                os.system(f"gnome-terminal -e {query}")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"it is {strTime} according to my clock")
                print(f"it is {strTime} according to my clock")

            elif 'drop my needle' in query:
                if "spotify" in (i.name() for i in psutil.process_iter()):
                    os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play")
                else:
                    os.system("gnome-terminal -e spotify")
                    time.sleep(1.5)
                    os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Play")


            elif query == 'power of yourself':
                speak("bye bye")
                os.system("shutdown now")

            elif query == "reboot yourself":
                speak("see you in a jiffy")
                os.system("reboot")

            else:
                print("nothing to work on.....")

        elif query == "stop listening" or query == "some privacy":
            break



