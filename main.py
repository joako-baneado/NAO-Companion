# -*- coding: utf-8 -*-
import os
import logging
import json
import signal
from datetime import datetime

from conversational_interface import ConversationalInterface
from emotional_analyzer import EmotionalAnalyzer
from intention_analyzer import IntentionAnalyzer, Intention
from empathetic_response_generator import EmpatheticResponseGenerator
from respuestas import respuestas
#from nao_robot_gestures import NAORobotGestures

class NAOCompanion:
    def __init__(self):
        self.conversational_interface = ConversationalInterface()
        self.emotional_analyzer = EmotionalAnalyzer()
        self.intention_analyzer = IntentionAnalyzer()
        self.response_generator = EmpatheticResponseGenerator(respuestas)
        #self.robot_gestures = NAORobotGestures()
        self.interactions = []
        self.session_active = True

        # Crear automáticamente la carpeta logs si no existe
        os.makedirs("logs", exist_ok=True)
        # Logging
        logging.basicConfig(
            filename='logs/session.log',
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s]: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        signal.signal(signal.SIGINT, self._handle_interrupt)

    def start_session(self):
        logging.info("🟢 Sesión iniciada")
        self.conversational_interface.speak("Hola, soy NAO, tu asistente emocional. ¿Cómo te sientes hoy?")

        while self.session_active:
            try:
                user_input = self.conversational_interface.transcribe_audio()
                if self._is_exit_command(user_input):
                    break
                self._process_user_input(user_input)
            except Exception as e:
                logging.exception("Error procesando entrada del usuario: {e}")
                self.conversational_interface.speak("Ocurrió un error. ¿Puedes repetir por favor?")

        self._end_session()

    def _process_user_input(self, user_input):
        emotion, conf_emotion = self.emotional_analyzer.analyze(user_input)
        intention, conf_intention = self.intention_analyzer.analyze(user_input)
        escalation = self._needs_escalation(emotion, intention)
        response = self.response_generator.generate(emotion, intention)

        # Gesto y respuesta hablada
        self.robot_gestures.perform(emotion)
        self.conversational_interface.speak(response)


    def _needs_escalation(self, emotion, intention):
        return emotion == "tristeza" and intention == "PROBLEMAS_PERSONALES"

    def _is_exit_command(self, user_input):
        return any(exit_word in user_input.lower() for exit_word in ["adiós", "chau", "terminar", "salir"])

    def _end_session(self):
        self.conversational_interface.speak("Gracias por conversar conmigo. ¡Cuídate mucho!")
        self._generate_session_report()
        logging.info("🔴 Sesión finalizada")

    def _generate_session_report(self):
        if not self.interactions:
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = "reports/session_report_"+timestamp+".json"

        emotions = [i.detected_emotion for i in self.interactions]
        intentions = [i.detected_intention for i in self.interactions]
        escalations = sum(i.escalation_needed for i in self.interactions)

        report = {
            "session_timestamp": timestamp,
            "total_interactions": len(self.interactions),
            "emotion_frequency": {e: emotions.count(e) for e in set(emotions)},
            "intention_frequency": {i: intentions.count(i) for i in set(intentions)},
            "escalations": escalations,
            "average_confidence_emotion": round(sum(i.confidence_emotion for i in self.interactions) / len(self.interactions), 2),
            "average_confidence_intention": round(sum(i.confidence_intention for i in self.interactions) / len(self.interactions), 2)
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        logging.info("📁 Reporte de sesión guardado en ",filename)

    def _handle_interrupt(self, sig, frame):
        print("\n⚠️ Interrupción detectada. Finalizando sesión...")
        self.session_active = False

def main():
    assistant = NAOCompanion()
    assistant.start_session()

if __name__ == "__main__":
    main()
