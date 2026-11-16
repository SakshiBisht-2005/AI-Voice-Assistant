
from gtts import gTTS
import os
import time

def speak(text):

    print("\nGenerating speech...")

    # Convert text into speech
    tts = gTTS(
        text=text,
        lang="en",
        slow=False
    )

    # Save audio
    filename = "response.mp3"
    tts.save(filename)

    print("Playing AI response...")

    # Open MP3 using Windows default media player
    os.startfile(os.path.abspath(filename))

    print("Audio generated successfully!")
