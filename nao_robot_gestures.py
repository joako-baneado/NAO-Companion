from naoqi import ALProxy

def ejecutar_gesto(emocion, robot_ip="192.168.1.100", port=9559):
    motion = ALProxy("ALMotion", robot_ip, port)
    posture = ALProxy("ALRobotPosture", robot_ip, port)

    if emocion == "Alegría":
        posture.goToPosture("Stand", 0.5)
        motion.angleInterpolationWithSpeed("HeadYaw", 0.5, 0.2)  # pequeño giro
    elif emocion == "Tristeza":
        motion.angleInterpolationWithSpeed("HeadPitch", 0.3, 0.2)  # cabeza hacia abajo
    elif emocion == "Ira":
        motion.angleInterpolationWithSpeed("HeadYaw", -0.5, 0.2)  # niega con la cabeza
    elif emocion == "Miedo":
        posture.goToPosture("Crouch", 0.5)
    elif emocion == "Ansiedad" or emocion == "Estrés":
        motion.angleInterpolationWithSpeed("HeadPitch", 0.2, 0.3)
    else:
        posture.goToPosture("StandInit", 0.5)



"""
from naoqi import ALProxy
import time

# Configura la IP de tu robot NAO
NAO_IP = "192.168.1.100"  # CAMBIA esto por la IP de tu robot
PORT = 9559

def saludo_robot():
    try:
        motion = ALProxy("ALMotion", NAO_IP, PORT)
        posture = ALProxy("ALRobotPosture", NAO_IP, PORT)

        # Despierta al robot (lo activa si está en reposo)
        motion.wakeUp()

        # Pone al robot en postura inicial
        posture.goToPosture("StandInit", 0.5)

        # Mueve el brazo derecho para saludar
        names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]
        angles = [1.5, -0.3, 1.0, 0.5, 0.0]
        fractionMaxSpeed = 0.2
        motion.setAngles(names, angles, fractionMaxSpeed)

        # Movimiento de cabeza (mirar al frente y luego hacia ti)
        motion.setAngles("HeadYaw", 0.0, 0.2)   # Centro
        motion.setAngles("HeadPitch", -0.2, 0.2)  # Ligeramente arriba

        time.sleep(2)

        # Regresa brazo a posición inicial
        motion.setAngles(names, [1.4, 0.0, 1.0, 0.0, 0.0], 0.2)

        # Postura final
        posture.goToPosture("Stand", 0.5)

    except Exception as e:
        print("Error en saludo:", e)

if __name__ == "__main__":
    saludo_robot()
"""
