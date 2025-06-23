# -*- coding: utf-8 -*-
from naoqi import ALProxy
import sys

def ejecutar_gesto(emocion, robot_ip="192.168.1.100", port=9559):
    motion = ALProxy("ALMotion", robot_ip, port)
    posture = ALProxy("ALRobotPosture", robot_ip, port)

    if emocion == "Alegria":
        posture.goToPosture("Stand", 0.5)
        motion.angleInterpolationWithSpeed("HeadYaw", 0.5, 0.2)  # pequeño giro
    elif emocion == "Tristeza":
        motion.angleInterpolationWithSpeed("HeadPitch", 0.3, 0.2)  # cabeza hacia abajo
    elif emocion == "Ira":
        motion.angleInterpolationWithSpeed("HeadYaw", -0.5, 0.2)  # niega con la cabeza
    elif emocion == "Miedo":
        posture.goToPosture("Crouch", 0.5)
    elif emocion == "Ansiedad" or emocion == "Estres":
        motion.angleInterpolationWithSpeed("HeadPitch", 0.2, 0.3)
    else:
        posture.goToPosture("StandInit", 0.5)


emotion = sys.stdin.read() 
ejecutar_gesto(emotion)

