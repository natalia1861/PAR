import speech_recognition as sr
import os
import spacy
from gtts import gTTS
from spacytextblob.spacytextblob import SpacyTextBlob
import time

import tensorflow as tf
import keras

nlp = spacy.load("en_core_web_trf")  # more accurate
# nlp = spacy.load("es_dep_news_trf") # more accurate
# nlp = spacy.load('es_core_news_sm') # faster
nlp.add_pipe("spacytextblob")  # only works for english models, not Spanish ones yet!
recognizer = sr.Recognizer()


def sleep_for_seconds(seconds):
    time.sleep(seconds)


def listen():
    try:
        print("Recording for 4 seconds...")
        with sr.Microphone() as source:
            print("Adjusting noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Recording...")
            recorded_audio = recognizer.listen(source, timeout=4)
            print("Done recording.")

            try:
                print("Recognizing the text...")
                text = recognizer.recognize_google(recorded_audio, language="en-US")
                print("Decoded Text: {}".format(text))
                return text.strip()

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio.")

            except sr.RequestError:
                print(
                    "Could not request results from Google Speech Recognition service."
                )

            except Exception as ex:
                print("Error during recognition:", ex)

    except Exception as e:
        print("Error during listening:", e)


def speak(text):
    # tts = gtts.gTTs(text=text, lang="en", slow=False)
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save("temp_audio.mp3")
    os.system("start temp_audio.mp3")
    # os.system("start temp_audio.mp3")
    os.remove("temp_audio.mp3")


def on_google_speech_recognition(text):
    doc = nlp(text)
    print("You said:")
    print("Words:", [token.text for token in doc])
    print("Sentiment polarity: ", doc._.polarity)
    print("Sentiment subjectivity: ", doc._.subjectivity)
    speak(text)


def on_execution_exception(ex):
    print("Error during execution:", ex)


def main_loop():
    while True:
        try:
            text = listen()
            if text:
                on_google_speech_recognition(text)
                sleep_for_seconds(8)
                # os.system(text)
        except Exception as e:
            on_execution_exception(e)


if __name__ == "__main__":
    main_loop()
