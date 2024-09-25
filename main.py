import speech_recognition as sr
import pyttsx3
import webbrowser
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open('https://www.google.com')
    elif "open facebook" in c.lower():
        webbrowser.open('https://www.facebook.com')
    elif "open youtube" in c.lower():
        webbrowser.open('https://www.youtube.com')
    elif "open github" in c.lower():
        webbrowser.open('https://www.github.com')    

if __name__ == "__main__":
    speak("Initializing Lexa...")
    
    while True:
        print("Recognizing...")
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                print("You said:", word)
                
                # If you say "alexa", system replies "Ya"
                if word.lower() == 'alexa':
                    speak('Ya')
                    print("Alexa active")

                    # Second listening for the command
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        try:
                            command = recognizer.recognize_google(audio)
                            print("You said command:", command)

                            processCommand(command)
                        except sr.UnknownValueError:
                            print("Sorry, I could not understand the command.")
                        except sr.RequestError as e:
                            print(f"Could not request results from Google Speech Recognition service; {e}")

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        
        except Exception as e:
            print(f"Error: {e}")
