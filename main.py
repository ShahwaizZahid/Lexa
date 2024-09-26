import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
import client
from gtts import gTTS
import pygame
import time
import os
import pyjokes
import weatherInfo
from dotenv import load_dotenv

load_dotenv()

ApiKey = os.getenv('ApiKey')

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")  # Replace 'your_file.mp3' with the path to your MP3 file

    # Play the MP3 file
    pygame.mixer.music.play()

    # Optional: Keep the script running while the music is playing
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    # Alternatively, you can use input to wait for user action
    # input("Press Enter to stop the music...")
    pygame.mixer.music.stop()  # Stop the music if you need to

    # Quit the mixer
    pygame.mixer.quit()
    
    os.remove('temp.mp3')

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def processCommand(c):
    print("Your command:", command)

    if "open google" in c.lower():
        webbrowser.open('https://www.google.com')
    elif "open facebook" in c.lower():
        webbrowser.open('https://www.facebook.com')
    elif "open youtube" in c.lower():
        webbrowser.open('https://www.youtube.com')
    elif "open github" in c.lower():
        webbrowser.open('https://www.github.com')
    elif "open facebook" in c.lower():
        webbrowser.open('https://www.facebook.com')
    elif c.lower().startswith('play'):
        song = c.lower().split(' ')[1]
        link = musicLibrary.music[song]  
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={ApiKey}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    elif "weather" in c.lower():
        res = weatherInfo.Weather(c) 
        speak(res) 
    elif "tell me a joke" in c.lower():
        tell_joke()
    elif "what time is it" in c.lower():
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    else:
     output = client.google_search(c) 
     speak(output)          

# speak(re)        
if __name__ == "__main__":
    speak("Initializing Lexa...")
    
    while True:
        print("Recognizing...")
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                
                # If you say "alexa", system replies "Ya"
                if word.lower() == 'alexa':
                    speak('Ya')
                    print("Alexa active speak command")

                    # Second listening for the command
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        try:
                            command = recognizer.recognize_google(audio)

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
