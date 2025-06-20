# -*- coding: utf-8 -*-
from naoqi import ALProxy
import time

class NAOAudioRecorder:
    def __init__(self, ip, port=9559):
        self.nao_ip = ip
        self.nao_port = port
        self.output_path = "/home/nao/recordings/audio.wav"
        self.recorder = ALProxy("ALAudioRecorder", self.nao_ip, self.nao_port)

    def record_audio(self, duration=5):
        channels = [1, 1, 0, 0]  # Usar micrófonos frontales
        sample_rate = 16000

        print("Comenzando grabación...")
        self.recorder.startMicrophonesRecording(self.output_path, "wav", sample_rate, channels)
        time.sleep(duration)
        self.recorder.stopMicrophonesRecording()
        print("Grabación finalizada. Archivo guardado en:", self.output_path)

    def get_audio_path(self):
        return self.output_path
