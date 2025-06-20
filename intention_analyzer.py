# -*- coding: utf-8 -*-
import re
import joblib
from enum import Enum
from typing import Tuple


class IntentionAnalyzer:
    def __init__(self, model_path="./models/intention_model.pkl"):
        self.model = joblib.load(model_path)

    def clean_text(self, text: str) -> str:
        return re.sub(r"[^\w\s]", "", text.lower())

    def analyze(self, text: str) -> Tuple[str, float]:
        cleaned_text = self.clean_text(text)
        proba = self.model.predict_proba([cleaned_text])[0]
        pred_index = proba.argmax()
        pred_label = self.model.classes_[pred_index]
        confidence = round(proba[pred_index], 2)


        return (pred_label, confidence)
