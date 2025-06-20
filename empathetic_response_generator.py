class EmpatheticResponseGenerator:
    def __init__(self, respuestas):
        self.respuestas = respuestas
        self.respuesta_generica = (
            "Gracias por compartir lo que sientes. No estoy seguro de cómo describir esa emoción, "
            "pero estoy aquí para escucharte y acompañarte."
        )

    def generate(self, emocion, intencion):
        emocion = emocion.upper()
        if emocion in self.respuestas:
            respuestas_emocion = self.respuestas[emocion]
            print(respuestas_emocion.get(intencion, respuestas_emocion))
            return respuestas_emocion.get(intencion, respuestas_emocion)
        else:
            return self.respuesta_generica

