import os
from askme.settings import BASE_DIR
import speech_recognition as sr


def rec_to_text():
    with open(os.path.join(BASE_DIR, "askme_api/assets/text_recognition.json")) as f:
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

    r = sr.Recognizer()

    name = 'askme/assets/file.wav'
    # Load audio file
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    # Transcribe audio file
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    with open(os.path.join(BASE_DIR, "askme/assets/transcript.txt", "w")) as f:
        f.write(text)
    return text
