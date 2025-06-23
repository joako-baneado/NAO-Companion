# -*- coding: utf-8 -*-
from naoqi import ALProxy
import time
import sys
import re

nao_ip = "192.168.219.36"
nao_port = 9559
output_path = "/home/nao/recordings/audio.wav"
tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
tts.setLanguage("Spanish")

text = sys.stdin.read() 

frases = re.split(r'[.,]', text)
for frase in frases:
    frase = frase.strip()
    if frase:
        tts.say(frase)
        
#tts.say(text)
