# Camara.py
from datetime import datetime

def encender_camara(camara):
    camara["estado"] = "encendida"
    print(f"Cámara {camara['id']} encendida.")

def apagar_camara(camara):
    camara["estado"] = "apagada"
    print(f"Cámara {camara['id']} apagada.")

def consultar_estado(camara):
    return camara["estado"]

def capturar_evento(camara, tipo_evento):
    evento = {
        "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo_evento
    }
    camara["registro_eventos"].append(evento)
    print(f"Evento capturado: {tipo_evento} en cámara {camara['id']}.")