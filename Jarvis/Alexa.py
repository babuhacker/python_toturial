import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak('hi i am your alexa ')



def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass



def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt('playing')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('current time is' + time)


run_alexa()
