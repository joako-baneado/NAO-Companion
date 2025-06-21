from naoqi import ALProxy
import time
import sys

nao_ip = "192.168.108.36"
nao_port = 9559
output_path = "/home/nao/recordings/audio.wav"
tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)

text = sys.stdin.read() 
tts.say(text)
