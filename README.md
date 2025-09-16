🎶 FRIDAY – Voice Assistant for Mohit

A Python-based voice assistant that greets Mohit, wishes him happy birthday on his special day, and can also play (and stop) his favorite song based on voice commands.

This project combines:
✅ Text-to-Speech (gTTS) for natural voice output.
✅ Speech Recognition for listening to Mohit’s commands.
✅ Pygame Mixer for playing songs.
✅ Automation (greets on startup, personalized interaction).

✨ Features

👋 Personalized Greeting: Says Hello Mohit, I am FRIDAY.

🎂 Birthday Wish: On 12th of the month, wishes Happy Birthday Mohit.

🎧 Voice-Interactive Music Player:

Asks if you want to play a song.

Plays song.mp3 if you say "yes".

Stops the music when you say "mute".

🗣️ Voice Recognition: Listens and understands commands using your microphone.

🕒 Real-Time Control: Keeps listening while music is playing.

📂 Requirements

Python 3.x

gTTS
 → Text-to-speech

pygame
 → Music playback

SpeechRecognition
 → Voice input

Microphone (for real-time speech commands)

⚙️ Installation
# Clone this repository
git clone https://github.com/yourusername/friday-assistant.git
cd friday-assistant

# Install dependencies
pip install gTTS pygame SpeechRecognition


⚠️ On Linux (Fedora/Ubuntu), also install:

sudo dnf install portaudio-devel    # Fedora
sudo apt-get install portaudio19-dev python3-pyaudio   # Ubuntu/Debian
pip install pyaudio

▶️ Usage

Save your favorite song as song.mp3 in the same folder as the script.

Run the assistant:

python friday.py


Interaction flow:

FRIDAY greets you.

If today is 12th, FRIDAY wishes you Happy Birthday.

FRIDAY asks: "Do you want me to play your favorite song?"

Say "yes" → Song starts playing.

While the song is playing, say "mute" → FRIDAY stops it.

🧩 Code Explanation
speak(text)

Converts text to speech using gTTS, saves as output.mp3, and plays it with pygame.

listen()

Activates the microphone, listens to your voice, and converts it into text using Google Speech Recognition.

greet() / wish()

Checks today’s date.

If not 12 → Greets Mohit.

If 12 → Wishes Happy Birthday.

ask_song()

Asks if Mohit wants to play music, listens for yes/no, and acts accordingly.

play_song()

Plays song.mp3. Keeps listening during playback. If you say "mute", FRIDAY stops the music.

🎯 Customization

Change the greeting/wish in speak() calls.

Replace song.mp3 with your own favorite track.

Adjust pause sensitivity with recognizer.pause_threshold.

For offline speech recognition, replace recognize_google with recognize_sphinx.

🚀 Future Ideas

Add more voice commands ("pause", "resume", "next song").

Replace gTTS with pyttsx3 for offline TTS.

Run automatically on system startup.

Integrate with APIs (weather, news, calendar).

📸 Demo Flow
FRIDAY: Hello Mohit, I am FRIDAY.
FRIDAY: Do you want me to play your favorite song?
You: yes
FRIDAY: Enjoy your favourite song.
🎶 (song.mp3 plays)
You: mute
FRIDAY: Okay, I am stopping this song.


✨ Now you have your own Jarvis-like personal assistant named FRIDAY!