# -*- coding: utf-8 -*-
import speech_recognition as sr
import pyttsx3

class ConversationalInterface:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

    def speak(self, texto):
        print(f"[Robot dice]: {texto}")
        self.tts_engine.say(texto)
        self.tts_engine.runAndWait()

    def transcribe_audio(self, audio_path="audio.wav"):
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)

            print("Transcribiendo con Google Speech Recognition...")
            texto = self.recognizer.recognize_google(audio, language="es-ES")
            print("Texto transcrito:")
            print(texto)
            return texto
        except sr.UnknownValueError:
            print("Google no pudo entender el audio.")
            return ""
        except sr.RequestError as e:
            print("Error al conectarse a Google:", e)
            return ""
        except Exception as e:
            print(f"Error inesperado: {e}")
            return ""
