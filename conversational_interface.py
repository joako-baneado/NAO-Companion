# -*- coding: utf-8 -*-
import speech_recognition as sr

# Crear un reconocedor
r = sr.Recognizer()

# Cargar archivo de audio .wav (debe estar en formato PCM 16kHz)
with sr.AudioFile("audio.wav") as source:
    audio = r.record(source)

print("Transcribiendo con Google Speech Recognition...")

try:
    texto = r.recognize_google(audio, language="es-ES")  # español
    print("Texto transcrito:")
    print(texto)
except sr.UnknownValueError:
    print("Google no pudo entender el audio.")
except sr.RequestError as e:
    print("Error al conectarse a Google:", e)
