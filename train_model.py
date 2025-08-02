import numpy as np
from sklearn.ensemble import IsolationForest
from joblib import dump

# Simular datos de entrenamiento
X_train = np.random.normal(loc=50, scale=10, size=(100, 2))  # CPU y RAM

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_train)

# Guardar modelo entrenado
dump(model, 'model.joblib')
print("[✔] Modelo entrenado y guardado como model.joblib")
