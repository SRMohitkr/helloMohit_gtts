import time
from gtts import gTTS
from pygame import mixer
import os
import speech_recognition as sr
currenttime = time.localtime()

def speak(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(filename)

    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    
    while mixer.music.get_busy():
        time.sleep(0.1)

    os.remove(filename)

def greet():
    if currenttime.tm_mday != 12:
        speak("Hello Mohit,I am FRIDAY")
        time.sleep(1)

def wish():
    if currenttime.tm_mday == 12:
        speak("Happy Birthday Mohit")
def listen():
    recognizer=sr.Recognizer()
    with sr.Recognizer.Microphone() as source:
        print("listening")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio,language='en-in')
            print("you_said:",text)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("⚠️ Google Speech service error")
            return ""

                                                                                                                     
def ask_song():
    speak("Do you want me to play your favorite song?")
    ans=listen()
    if "yes" in ans:
        speak("Enjoy your favourite song")
        play_song("song.mp3")
    else:
        speak("Okay, maybe next time.")
    time.sleep(2)    

def play_song(song_file):
    if not os.path.exists(song_file):
        speak("Sorry, the song file does not exist.")
        return
    mixer.init()
    mixer.music.load(song_file)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)
        cmd=listen()
        if "mute" in cmd:
            mixer.music.stop()
            speak("okay,I am stoping this song.")
            break    


if __name__ == "__main__":
    greet()
    ask_song()
    wish()
