# -*- coding: utf-8 -*-
import speech_recognition as sr
import paramiko
import os
import subprocess
import requests
import time

class ConversationalInterface:

    
    def __init__(self, nao_ip="192.168.108.36",nao_port = 9559, nao_user="nao", nao_pass="nao"):
        self.recognizer = sr.Recognizer()
        self.nao_ip = nao_ip
        self.nao_user = nao_user
        self.nao_pass = nao_pass
        self.nao_port = nao_port
        self.remote_path = "/home/nao/audio.wav"
        self.local_path = "./audio.wav"

    def grabar_con_nao(self):
            print("🎙️ Ejecutando grabación en NAO...")
            try:
                subprocess.run(["C:/Python27/python.exe", "nao_record.py"])  # Usa python2 o la ruta exacta a tu Python 2.7
            except Exception as e:
                print("❌ Error al grabar audio con NAO:", e)

    def download_audio(self):
        url = f"http://{self.nao_ip}:{self.nao_port}/audio.wav"
        try:
            time.sleep(2)
            response = requests.get(url)
            with open(self.local_path, "wb") as f:
                f.write(response.content)
            print("✅ Audio descargado vía HTTP")
            return True
        except Exception as e:
            print("❌ Error al descargar audio vía HTTP:", e)
            return False
        
    def hablartexto():
        texto = input("Escriba por acá: ")
        return texto
    
    def transcribe_audio(self, audio_path="audio.wav"):
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
            print("Transcribiendo...")
            texto = self.recognizer.recognize_google(audio, language="es-ES")
            print("Transcripción:", texto)
            return texto
        except sr.UnknownValueError:
            print("Google no entendió el audio.")
            return ""
        except sr.RequestError as e:
            print("Error al conectar a Google:", e)
            return ""

    def speak(self, text):

        print("🗣️ NAO dice:", text)
        subprocess.run(
            ["C:/Python27/python.exe", "nao_speak.py"],
            input=text,
            capture_output=False,  # Captura stdout y stderr
            text=True,
            timeout=10  # Opcional: evita que se congele si hay problemas
        )
       
