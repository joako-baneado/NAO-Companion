# -*- coding: utf-8 -*-
import speech_recognition as sr
import paramiko
import os
import subprocess

class ConversationalInterface:

    
    def __init__(self, nao_ip="192.168.1.100", nao_user="nao", nao_pass="nao"):
        self.recognizer = sr.Recognizer()
        self.nao_ip = nao_ip
        self.nao_user = nao_user
        self.nao_pass = nao_pass
        self.remote_path = "/home/nao/recordings/audio.wav"
        self.local_path = "audio.wav"

    def grabar_con_nao(self):
            print("🎙️ Ejecutando grabación en NAO...")
            try:
                subprocess.call(["python2", "audio_nao.py"])  # Usa python2 o la ruta exacta a tu Python 2.7
            except Exception as e:
                print("❌ Error al grabar audio con NAO:", e)

    def download_audio(self):
        print("⬇Descargando audio desde NAO...")
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.nao_ip, username=self.nao_user, password=self.nao_pass)
            sftp = ssh.open_sftp()
            sftp.get(self.remote_path, self.local_path)
            sftp.close()
            ssh.close()
            print("Audio descargado en:", self.local_path)
            return True
        except Exception as e:
            print("Error al descargar el audio:", e)
            return False

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
       
