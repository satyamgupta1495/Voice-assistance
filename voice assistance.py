import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hii satyam I am your personal assistant  how may I help you!")


def takecommand():
    # take microphone ip frm user and returns string op

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")

        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing....")
            # google se help le rha h
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
            # print(e)

            print("say that again.....")
            return "None"

        return query


if __name__ == "__main__":
    wishme()
    while 1:
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:

            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open unsplash' in query:
            webbrowser.open("unsplash.com")

        elif 'play music' in query:
            music_dir = 'D:\\satyam\\mp3'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strtime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Satyam Gupta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'actor' in query:
            speak("Sir, lee min hoo is your favourite actor")

        elif 'favourite KD' in query:
            speak("Sir, Doctors is your favourite Korean Drama")

        elif 'Favourite country' in query:
            speak("Sir, Paris is your favourite country")

        elif 'like the most' in query:
            speak("Sir, Sleeping under the stary night sky is your favourite thing to do")
