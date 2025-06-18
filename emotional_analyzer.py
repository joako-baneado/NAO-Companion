import joblib
from typing import Dict, Tuple
from enum import Enum

class Emocion(Enum):
    ANSIEDAD = "ANSIEDAD"
    ALEGRIA = "ALEGRIA"
    ESTRES = "ESTRES"
    TRISTEZA = "TRISTEZA"
    IRA = "IRA"
    MIEDO = "MIEDO"
    NEUTRO = "NEUTRO"

class EmotionalAnalyzer:
    def __init__(self, model_path="model.pkl"):
        self.model = joblib.load(model_path)
        self.labels = self.model.classes_

    def detect_emotion_distribution(self, text: str) -> Tuple[str, float, Dict[str, float]]:
        """
        Analiza el texto y retorna:
        - emoción predominante
        - confianza (0.0 a 100.0)
        - distribución completa (emoción: porcentaje)
        """
        if not text or len(text.strip()) < 5:
            return "Neutro", 0.0, {label: 0.0 for label in self.labels}

        probs = self.model.predict_proba([text])[0]
        distribution = {label: round(prob * 100, 2) for label, prob in zip(self.labels, probs)}

        # Obtener emoción dominante y su porcentaje
        max_idx = probs.argmax()
        top_emotion = self.labels[max_idx]
        top_confidence = round(probs[max_idx] * 100, 2)

        return top_emotion, top_confidence, distribution

# 🔎 Ejemplo de uso
if __name__ == "__main__":
    analyzer = EmotionalAnalyzer()
    texto = input()
    
    emocion, confianza, distribucion = analyzer.detect_emotion_distribution(texto)
    
    print(f"Emoción predominante: {emocion}")
    print(f"Confianza: {confianza}%")
    print("Distribución emocional:")
    for e, p in distribucion.items():
        print(f"- {e}: {p}%")
