# -*- coding: utf-8 -*-
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

class IntentionAnalyzer:
    def __init__(self, model_path="./models/intention_model.pkl"):
        self.model = joblib.load(model_path)

    def clean_text(self, text: str) -> str:
        return re.sub(r"[^\w\s]", "", text.lower())

    def analyze(self, text: str) -> Tuple[Intention, float]:
        cleaned_text = self.clean_text(text)
        proba = self.model.predict_proba([cleaned_text])[0]
        pred_index = proba.argmax()
        pred_label = self.model.classes_[pred_index]
        confidence = round(proba[pred_index], 2)

        try:
            intent_enum = Intention[pred_label]
        except KeyError:
            intent_enum = Intention.SIN_INTENCION

        return (intent_enum, confidence)
