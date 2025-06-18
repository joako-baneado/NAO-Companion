class GeneradoRespuestas:
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


# Diccionario de respuestas
respuestas = {
    "ANSIEDAD": {
        "PROBLEMAS_ACADEMICOS": "Entiendo que enfrentarte a los cursos y tareas puede causarte ansiedad. Intenta organizar tu tiempo en bloques manejables y no tengas miedo de pedir ayuda. Confía en ti mismo/a, cada pequeño avance cuenta.",
        "ESTRES_EXAMENES": "Es normal sentir ansiedad ante los exámenes. Respira profundo, repasa lo esencial y cuida tu descanso. Has superado pruebas antes, y esta vez no será diferente. Tú puedes con esto.",
        "PROBLEMAS_PERSONALES": "Sé que tus problemas personales pueden generarte mucha ansiedad. Hablar con alguien cercano o tomarte un momento para ti puede ayudarte a liberar tensión. No estás solo/a y tienes la capacidad para salir adelante.",
        "FALTA_MOTIVACION": "Sentirse ansioso/a cuando no encuentras motivación es muy común. Empieza con tareas pequeñas, incluso si parecen mínimas. Tienes dentro de ti la fuerza necesaria para retomar el camino poco a poco.",
        "DUDAS_CARRERA": "Es comprensible sentir ansiedad si estás cuestionando tu carrera. Conversar con profesionales o personas de confianza puede darte claridad. Recuerda que replantear tu camino también es una forma de avanzar.",
        "PROBLEMAS_SOCIALES": "Las interacciones sociales pueden generar ansiedad. No pasa nada si necesitas espacio. Busca espacios donde te sientas seguro/a, con personas que te respeten. Con el tiempo, podrás sentirte más cómodo/a siendo tú mismo/a.",
        "SALUDO_GENERAL": "Hola, noto algo de ansiedad en tu tono. Estoy aquí para acompañarte. Hablar con alguien puede ayudarte a aliviar esa carga. Este es un buen paso, sigue expresándote con confianza.",
        "DESPEDIDA": "Gracias por compartir lo que sientes. Espero que esta charla haya aliviado un poco tu ansiedad. Recuerda que siempre puedes volver. Cuídate mucho.",
        "SIN_INTENCION": "Percibo que sientes ansiedad. Está bien, todos pasamos por momentos así. Tómate un respiro y cuida tu bienestar. Estoy contigo."
    },
    "TRISTEZA": {
        "PROBLEMAS_ACADEMICOS": "Sentirse triste por temas académicos es totalmente válido. Tal vez no todo salió como esperabas, pero siempre hay oportunidades de mejorar. Eres capaz y valioso/a, no dejes que una nota defina tu valía.",
        "ESTRES_EXAMENES": "Los exámenes pueden afectar tu estado de ánimo. Prepara lo que puedas, duerme bien, y habla con alguien si lo necesitas. Tu esfuerzo vale más que cualquier resultado.",
        "PROBLEMAS_PERSONALES": "Lamento que estés atravesando un momento difícil a nivel personal. Busca contención en quienes te rodean o en apoyo profesional. No estás solo/a, y este dolor no durará para siempre.",
        "FALTA_MOTIVACION": "La tristeza puede apagar la motivación. Haz cosas pequeñas que te traigan algo de bienestar. No te exijas demasiado. Avanzar lento también es avanzar. Estoy contigo.",
        "DUDAS_CARRERA": "Es normal sentir tristeza al no tener claro tu futuro. Reflexionar no es una debilidad, sino un acto de madurez. Sigue explorando tus pasiones, el camino se aclarará.",
        "PROBLEMAS_SOCIALES": "Sentirse solo/a en la universidad puede ser doloroso. Intenta acercarte poco a poco a personas o espacios afines. Tu compañía vale mucho, incluso si ahora no lo ves.",
        "SALUDO_GENERAL": "Hola. Si estás pasando por un mal momento, estoy aquí para escucharte. Tu bienestar me importa, y puedes confiar en este espacio para desahogarte. Tienes derecho a sentirte triste y también a sanar.",
        "DESPEDIDA": "Gracias por compartir tus emociones. Espero que esta conversación haya sido un alivio. Cuídate mucho, y recuerda que siempre puedes volver si lo necesitas.",
        "SIN_INTENCION": "Parece que sientes tristeza. Está bien reconocerlo. Haz algo pequeño por ti hoy, y permítete descansar. No estás solo/a. Aquí estoy para acompañarte."
    },
    "ESTRES": {
        "PROBLEMAS_ACADEMICOS": "Entiendo que los trabajos y tareas pueden abrumarte. Haz una lista de prioridades y enfócate en lo más urgente. Tienes la capacidad para manejarlo, paso a paso.",
        "ESTRES_EXAMENES": "Los exámenes generan mucho estrés. Descansa, repasa en bloques y no olvides respirar. No necesitas ser perfecto/a para hacerlo bien. Confía en lo que sabes.",
        "PROBLEMAS_PERSONALES": "Los temas personales también generan presión. Habla con alguien de confianza o busca un espacio seguro para desahogarte. Cuidarte emocionalmente también es una prioridad.",
        "FALTA_MOTIVACION": "El estrés constante puede hacerte perder motivación. Haz pausas, come bien, duerme lo necesario. Recargar energía te ayudará a reconectar con tus metas.",
        "DUDAS_CARRERA": "Dudar de tu carrera puede ser estresante. Busca orientación vocacional o habla con profesionales del área. Estás construyendo tu camino y eso lleva tiempo.",
        "PROBLEMAS_SOCIALES": "Las relaciones sociales pueden ser fuente de estrés. No te obligues a encajar. Sé tú mismo/a y rodéate de personas que te valoren. No estás obligado/a a agradar a todos.",
        "SALUDO_GENERAL": "Hola, percibo cierto estrés en ti. Si quieres hablar, estoy disponible para escucharte. Tomarte este tiempo ya es un buen paso para sentirte mejor.",
        "DESPEDIDA": "Gracias por darte un momento para conversar. Deseo que encuentres calma en lo que viene. Cuídate mucho.",
        "SIN_INTENCION": "Parece que estás bajo estrés. Trata de hacer una pausa consciente. Tu bienestar importa y no todo debe resolverse hoy. Respira."
    },
    "ALEGRIA": {
        "PROBLEMAS_ACADEMICOS": "Es genial que a pesar de los retos académicos sigas manteniendo una actitud positiva. Esa energía te ayudará a superarlos. ¡Sigue así!",
        "ESTRES_EXAMENES": "Me alegra ver que enfrentas los exámenes con entusiasmo. Con esa actitud, tienes muchas más chances de triunfar.",
        "PROBLEMAS_PERSONALES": "Me alegra saber que, pese a los desafíos personales, encuentras motivos para sonreír. Esa fuerza interior es muy valiosa.",
        "FALTA_MOTIVACION": "¡Qué bien que hayas recuperado la motivación! Recuerda lo que te impulsa y úsalo como combustible para seguir creciendo.",
        "DUDAS_CARRERA": "Incluso con dudas, mantener alegría es admirable. Explora lo que te inspira y ve descubriendo tu camino con confianza.",
        "PROBLEMAS_SOCIALES": "Encontrar alegría en medio de relaciones complejas muestra tu fortaleza emocional. Sigue cultivando lo que te hace sentir bien.",
        "SALUDO_GENERAL": "¡Hola! Me alegra mucho que estés con buen ánimo. Aprovecha este estado para disfrutar y compartir con quienes quieres. Tu energía positiva es contagiosa. ¡Sigue así!",
        "DESPEDIDA": "¡Qué gusto haber compartido este momento contigo! Sigue sonriendo y haciendo lo que te hace bien. Hasta pronto.",
        "SIN_INTENCION": "¡Es hermoso ver que te sientes alegre! Guarda este momento como un recuerdo bonito. Tu alegría también inspira a otros. ¡Disfrútalo!"
    },
    "IRA": {
        "PROBLEMAS_ACADEMICOS": "Es comprensible que ciertas situaciones académicas te generen ira. Trata de canalizar esa energía en acciones productivas. Tu voz y tus emociones son válidas.",
        "ESTRES_EXAMENES": "A veces el estrés por los exámenes se convierte en enojo. Haz pausas, respira, y no te exijas más de lo que puedes dar. Estás haciendo lo mejor que puedes.",
        "PROBLEMAS_PERSONALES": "Las relaciones personales pueden provocar mucha frustración. Habla desde lo que sientes, sin culpar. Mereces paz y respeto en tus vínculos.",
        "FALTA_MOTIVACION": "Estar enojado/a contigo mismo/a por no avanzar es común. Sé compasivo/a con tu proceso. Cada paso cuenta.",
        "DUDAS_CARRERA": "La confusión y la frustración sobre el futuro pueden generar ira. Reflexionar y hablarlo te ayudará a aclarar tus ideas.",
        "PROBLEMAS_SOCIALES": "Sentirte incomprendido/a en lo social puede ser molesto. Expresa tus emociones sin dañar. Rodéate de personas que te valoren.",
        "SALUDO_GENERAL": "Hola, si sientes enojo, estoy aquí para escucharte sin juzgar. Hablar sobre lo que molesta puede ser un primer paso para liberarlo.",
        "DESPEDIDA": "Gracias por hablar desde lo que sientes. Espero que encuentres calma después de este momento. Te deseo serenidad.",
        "SIN_INTENCION": "Parece que algo te tiene irritado/a. Está bien expresarlo. Respira, suéltalo, y date permiso de descansar emocionalmente."
    },
    "MIEDO": {
        "PROBLEMAS_ACADEMICOS": "Los retos académicos pueden darte miedo. Enfrenta uno por uno, pide ayuda cuando la necesites. Eres capaz, aunque tengas dudas.",
        "ESTRES_EXAMENES": "El miedo a fallar en exámenes es natural. Estudia con calma y cree en lo que sabes. Cada intento es una oportunidad de crecer.",
        "PROBLEMAS_PERSONALES": "Lo personal puede dar miedo, especialmente si sientes que pierdes el control. Busca apoyo, no estás solo/a. Puedes con esto.",
        "FALTA_MOTIVACION": "El miedo a no avanzar puede paralizar. Muévete despacio, pero sigue. No necesitas ir rápido para llegar.",
        "DUDAS_CARRERA": "Tener miedo al futuro profesional es común. Evalúa tus opciones y escucha tu intuición. Construirás tu camino paso a paso.",
        "PROBLEMAS_SOCIALES": "Socializar puede dar miedo. Da pequeños pasos y sé tú mismo/a. No necesitas forzar nada.",
        "SALUDO_GENERAL": "Hola. Si estás sintiendo miedo, quiero que sepas que aquí hay un espacio seguro. Tu valentía ya se nota al abrirte a conversar.",
        "DESPEDIDA": "Gracias por compartir tus temores. Espero que te sientas un poco más acompañado/a. No dejes que el miedo te impida avanzar.",
        "SIN_INTENCION": "Siento que algo te asusta. Está bien tener miedo. Ámate en medio de esa emoción y busca tranquilidad dentro de ti."
    },
    "NEUTRO": {
        "PROBLEMAS_ACADEMICOS": "A veces podemos sentirnos neutros frente a lo académico. Eso también está bien. Observa y reflexiona desde ese estado.",
        "ESTRES_EXAMENES": "Si te sientes en equilibrio antes del examen, aprovéchalo. Esa calma puede ser tu mejor aliada.",
        "PROBLEMAS_PERSONALES": "Estar emocionalmente neutro frente a lo personal puede ayudarte a tomar decisiones. Confía en tu capacidad de observar sin juicio.",
        "FALTA_MOTIVACION": "La neutralidad a veces es antesala de un cambio. Reflexiona con calma sobre lo que deseas retomar.",
        "DUDAS_CARRERA": "Estar en pausa emocional respecto a tu carrera puede darte perspectiva. Escucha tus pensamientos sin presión.",
        "PROBLEMAS_SOCIALES": "Sentirse neutral en lo social está bien. No siempre tenemos que buscar algo. Solo sé tú mismo/a.",
        "SALUDO_GENERAL": "Hola. Qué bueno que te encuentres en equilibrio. Aquí estoy si deseas compartir algo o simplemente conversar.",
        "DESPEDIDA": "Gracias por tu tiempo. Espero que sigas manteniendo ese equilibrio emocional. Hasta pronto.",
        "SIN_INTENCION": "Parece que estás en un momento estable. Disfruta de esa neutralidad. El equilibrio también es parte del bienestar."
    }
}

# Crear instancia y probar
banco = GeneradoRespuestas(respuestas)

# Ejemplo de prueba
print(banco.obtener_respuesta("alegria", "problemas_personales"))
print(banco.obtener_respuesta("enojo", "problemas_academicos"))  # emoción no reconocida
print(banco.obtener_respuesta("", "falta_motivacion"))           # emoción vacía
print(banco.obtener_respuesta("tristeza", ""))                   # intención vacía → usa SIN_INTENCION
