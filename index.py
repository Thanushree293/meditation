import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

r = sr.Recognizer()
with sr.Microphone() as source:
    print('listening....')
    r.pause_threshold = 1
    audio = r.listen(source, timeout=10, phrase_time_limit=13)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str ="speak now"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str =" sorry couldnt recognize"
            speak(str)

def Balenq():
    speak("Enter the PIN ")
    a=listen()
    input(a)
    speak("the balance is 345")

def WithdrawAmount():
    speak ("Enter the PIN ")
    b=listen()
    input(b)
    speak("collect your cash ")

    while (1):
        str = "what do you want to do?"
        speak(str)
        str = "speak BALANCE to view your  balance     speak WITHDRAW to withdraw cash    speak EXIT to exit "
        speak(str)

    ch = listen()
    if (ch == 'balance'):
        str = "you have chose to view Balance"
        speak(str)
        Balenq()

    elif (ch == 'withdraw'):
        str = "you have chosen to withdraw"
        speak(str)
        WithdrawAmount()

    elif (ch == 'EXIT'):
        str = "you have chosen to exit"
        speak(str)
        exit(1)
    else:
        str = "Invalid choice,you said:"