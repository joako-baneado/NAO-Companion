# NAO Companion 🤖

NAO Companion es un asistente emocional implementado para el robot humanoide NAO. El sistema utiliza procesamiento de lenguaje natural para detectar emociones y generar respuestas empáticas, creando una experiencia de interacción más humana y cercana.

## 🎯 Características

- Reconocimiento de emociones en texto
- Análisis de intenciones del usuario
- Generación de respuestas empáticas contextualizadas
- Sistema de logging y reportes de interacciones
- Integración con gestos físicos del robot NAO
- Interfaz conversacional por texto y voz

## 🛠️ Requisitos Previos

- Python 2.7 (para NAOqi SDK)
- Python 3.8+ (para el sistema principal)
- NAO Robot con conectividad de red
- Sistema operativo: Windows/Linux/MacOS

## ⚙️ Configuración

1. Clonar el repositorio:
```bash
git clone https://github.com/joako-baneado/NAO-Companion.git
cd NAO-Companion
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar el robot NAO:
   - Asegúrate de que el robot esté en la misma red
   - Modifica la IP del robot en `nao_speak.py` si es necesario:
```python
nao_ip = "192.168.219.36"  # Cambia a la IP de tu robot
nao_port = 9559
```

4. Preparar modelos de ML:
```bash
python training/emotion_train_model.py
python training/intention_train_model.py
```

## 📂 Estructura del Proyecto

```
NAO-Companion/
├── main.py                      # Punto de entrada principal
├── conversational_interface.py  # Interfaz de conversación
├── emotional_analyzer.py        # Análisis de emociones
├── intention_analyzer.py        # Análisis de intenciones
├── nao_speak.py                # Control de voz del NAO
├── nao_robot_gestures.py       # Control de gestos del NAO
├── respuestas.py               # Base de respuestas empáticas
├── requirements.txt            # Dependencias del proyecto
├── models/                     # Modelos entrenados
├── training/                   # Scripts de entrenamiento
├── logs/                      # Registros de sesiones
└── reports/                   # Reportes generados
```

## 🚀 Uso

1. Iniciar el sistema:
```bash
python main.py
```

2. Interactuar con el robot:
   - Puedes escribir texto directamente
   - El sistema detectará emociones y generará respuestas
   - NAO responderá verbalmente y con gestos

3. Comandos de salida:
   - "adiós"
   - "chau"
   - "terminar"
   - "salir"

## 📊 Reportes

El sistema genera automáticamente reportes de sesión en formato JSON que incluyen:
- Timestamp de la sesión
- Total de interacciones
- Frecuencia de emociones detectadas
- Frecuencia de intenciones
- Casos de escalamiento
- Niveles de confianza promedio

## 🔍 Análisis de Emociones

El sistema puede detectar las siguientes emociones:
- Alegría
- Tristeza
- Ira
- Miedo
- Ansiedad
- Estrés

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ✨ Autores

- [@joako-baneado](https://github.com/joako-baneado)
- [@Maserattew](https://github.com/Maserattew)
- [@SebasTM502](https://github.com/SebasTM502)
- [@yagocz](https://github.com/yagocz)

## 📞 Soporte

Para reportar problemas o solicitar ayuda:
1. Abre un issue en GitHub
2. Describe el problema detalladamente
3. Incluye logs relevantes si es posible

---
⭐ Si este proyecto te ha sido útil, considera darle una estrella en GitHub!
