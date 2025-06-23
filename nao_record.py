# -*- coding: utf-8 -*-
from naoqi import ALProxy
import time

nao_ip = "192.168.108.36"
nao_port = 9559
output_path = "/home/nao/audio.wav"
recorder = ALProxy("ALAudioRecorder", nao_ip, nao_port)

def record_audio(duration=5):
    channels = [1, 0, 0, 0]  # Usar micrófonos frontales
    
    sample_rate = 16000

    print("Comenzando grabación...")
    #recorder.startMicrophonesRecording(output_path, "wav", sample_rate, channels)
    recorder.startMicrophonesRecording(output_path, "wav", sample_rate, channels)
    time.sleep(duration)
    recorder.stopMicrophonesRecording()
    print("Grabación finalizada. Archivo guardado en:", output_path)

record_audio()