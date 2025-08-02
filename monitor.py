import psutil
import numpy as np
from joblib import load
import time

model = load('model.joblib')
print("[🔍] Modelo cargado. Iniciando monitoreo...")

def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    return [cpu, mem]

while True:
    data = np.array(get_metrics()).reshape(1, -1)
    pred = model.predict(data)
    print(f"[INFO] CPU: {data[0][0]}%, Mem: {data[0][1]}% --> {'⚠ Anomalía' if pred[0] == -1 else 'OK'}")
    time.sleep(2)
