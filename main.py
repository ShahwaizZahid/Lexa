import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speck (text):
    engine.say(text)
    engine.runAndWait()

if __name__ =="__main__":
    speck("Initializing Lexa........")
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening.....")
            audio = r.listen(source)
        # recognize speech using Sphinx
        try:
            command = r.recognize_google_cloud(source)
            print(command)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))