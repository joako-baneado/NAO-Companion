import random
import time
from codigonao import iniciar_nao, escuchar, hablar
from emotional_analyser import analizar_emocion
from use_model import predecir_intencion
from empathetic_response_generator import generar_respuesta_empatica

def iniciar_interaccion():
    hablar("Hola, soy tu asistente emocional. ¿Cómo te sientes hoy?")

    while True:
        texto_usuario = escuchar()

        if texto_usuario:
            if any(palabra in texto_usuario for palabra in ["salir", "adiós", "chao"]):
                hablar("Gracias por compartir conmigo. Recuerda que no estás solo. Hasta luego.")
                break

            emocion = analizar_emocion(texto_usuario)
            intencion = predecir_intencion(texto_usuario)
            respuesta = generar_respuesta_empatica(emocion, intencion, texto_usuario)

            hablar(respuesta)
        else:
            hablar("No te entendí bien. ¿Puedes repetirlo?")
        time.sleep(1)

if __name__ == "__main__":
    iniciar_interaccion()
