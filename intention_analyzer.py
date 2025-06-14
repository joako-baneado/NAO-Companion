import re
import joblib
from enum import Enum
from typing import Tuple
import numpy as np

class Intention(Enum):
    PROBLEMAS_ACADEMICOS = "PROBLEMAS_ACADEMICOS"
    ESTRES_EXAMENES = "ESTRES_EXAMENES"
    PROBLEMAS_PERSONALES = "PROBLEMAS_PERSONALES"
    FALTA_MOTIVACION = "FALTA_MOTIVACION"
    DUDAS_CARRERA = "DUDAS_CARRERA"
    PROBLEMAS_SOCIALES = "PROBLEMAS_SOCIALES"
    SALUDO_GENERAL = "SALUDO_GENERAL"
    DESPEDIDA = "DESPEDIDA"
    SIN_INTENCION = "SIN_INTENCION"

# Cargar modelo
modelo = joblib.load("modelo_intencion.pkl")

def clean_text(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def detect_intention(text: str) -> Tuple[Intention, float]:
    cleaned_text = clean_text(text)
    proba = modelo.predict_proba([cleaned_text])[0]
    pred_index = proba.argmax()
    pred_label = modelo.classes_[pred_index]
    confidence = round(proba[pred_index], 2)

    try:
        intent_enum = Intention[pred_label]
    except KeyError:
        intent_enum = Intention.SIN_INTENCION

    return (intent_enum, confidence)

# Ejemplo de uso
if __name__ == "__main__":
    texto_usuario = input("Escribe tu mensaje: ")
    intencion, confianza = detect_intention(texto_usuario)
    print(f"🔎 Intención detectada: {intencion.value} | Confianza: {confianza}")
