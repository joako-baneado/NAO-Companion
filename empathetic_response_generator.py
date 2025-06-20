class EmpatheticResponseGenerator:
    def __init__(self, respuestas):
        self.respuestas = respuestas
        self.respuesta_generica = (
            "Gracias por compartir lo que sientes. No estoy seguro de cómo describir esa emoción, "
            "pero estoy aquí para escucharte y acompañarte."
        )

    def obtener_respuesta(self, emocion, intencion):
        if not emocion:
            return self.respuesta_generica

        emocion = emocion.upper()
        intencion = intencion.upper() if intencion else "SIN_INTENCION"

        if emocion in self.respuestas:
            respuestas_emocion = self.respuestas[emocion]
            return respuestas_emocion.get(intencion, respuestas_emocion.get("SIN_INTENCION", self.respuesta_generica))
        else:
            return self.respuesta_generica
