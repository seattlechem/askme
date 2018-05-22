import os
import speech_recognition as sr


def rec_to_text():
    with open("text-recognition-67c11381cd20.json") as f:
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

    r = sr.Recognizer()

    name = 'file.wav'
    # Load audio file
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    # Transcribe audio file
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    print(text)
    with open("transcript.txt", "w") as f:
        f.write(text)
    return text
