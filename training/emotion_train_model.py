import pandas as pd
import re
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

def limpiar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8')
    texto = re.sub(r"[^\w\s]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

# 1. Cargar dataset
df = pd.read_csv("C:/Users/Sebastian/Desktop/cloneRepoIA/NAO-Companion/training/emotion_dataset.csv")
df["text"] = df["text"].astype(str).apply(limpiar_texto)

# 2. Dividir
X = df["text"]
y = df["emotion"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# 3. Pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2), max_features=5000)),
    ("clf", LogisticRegression(max_iter=1000, solver="lbfgs", multi_class="multinomial"))
])

# 4. Entrenar y evaluar
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# 5. Guardar modelo
joblib.dump(pipeline, "model.pkl")
