
import sounddevice as sd
import speech_recognition as sr
import wave

def listen():
    sample_rate = 16000
    duration = 5

    print("Listening... Speak now!")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    with wave.open("input.wav", "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(sample_rate)
        file.writeframes(audio.tobytes())

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile("input.wav") as source:
            recorded_audio = recognizer.record(source)

        text = recognizer.recognize_google(
            recorded_audio,
            language="en-IN"
        )

        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None

    except sr.RequestError as error:
        print("Speech recognition error:", error)
        return None
