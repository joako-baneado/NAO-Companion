import pandas as pd
import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Preprocesamiento del texto
def clean_text(text):
    return re.sub(r"[^\w\s]", "", text.lower())

# Leer dataset
df = pd.read_csv("dataset.csv")
df["texto"] = df["texto"].apply(clean_text)

# Separar datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    df["texto"], df["intencion"], test_size=0.2, random_state=42, stratify=df["intencion"]
)

# Crear pipeline de entrenamiento
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=500))
])

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Guardar modelo
joblib.dump(pipeline, "modelo_intencion.pkl")
print("✅ Modelo entrenado y guardado como 'modelo_intencion.pkl'")

# Evaluación del modelo
y_pred = pipeline.predict(X_test)

print("\n📊 Reporte de Clasificación:")
print(classification_report(y_test, y_pred))
