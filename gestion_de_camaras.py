# gestion_de_camaras.py
from datetime import datetime

# Datos de las camaras (definido globalmente)
camaras = {
    "camara_1": {"ubicacion": "Entrada principal", "estado": "apagada", "configuracion": {}, "actividad": 10, "registro_eventos": [], "vision_nocturna": False},
    "camara_2": {"ubicacion": "Estacionamiento", "estado": "encendida", "configuracion": {}, "actividad": 5, "registro_eventos": [], "vision_nocturna": False}
}

def crear_camara(id_camara, ubicacion="desconocida"):
    camaras[id_camara] = {
        "id": id_camara,
        "estado": "apagada",
        "ubicacion": ubicacion,
        "configuracion": {},
        "actividad": 0,
        "registro_eventos": [],
        "vision_nocturna": False
    }
    print(f"Cámara {id_camara} creada en {ubicacion}.")

def listar_camaras():
    if not camaras:
        return "No hay cámaras disponibles."
    listado = ""
    for id_camara, datos in camaras.items():
        listado += f"ID: {id_camara}, Ubicación: {datos['ubicacion']}, Estado: {datos['estado']}\n"
    return listado.strip()


def eliminar_camara(camara_id):
    """
    Elimina una cámara del sistema.
    """
    if camara_id in camaras:
        del camaras[camara_id]

def modificar_camara(camara_id, nueva_configuracion):
    """
    Modifica la configuración de una cámara existente.
    """
    if camara_id in camaras:
        camaras[camara_id].update(nueva_configuracion)

def buscar_camara_por_ubicacion(ubicacion):
    """
    Devuelve una lista de cámaras que coinciden con la ubicación especificada.
    """
    return [cam for cam in camaras.values() if cam["ubicacion"] == ubicacion]

def ordenar_camaras_por_ubicacion():
    """
    Ordena las cámaras por ubicación y las devuelve en una lista.
    """
    return sorted(camaras.values(), key=lambda x: x["ubicacion"])

def obtener_camara_con_mayor_actividad():
    """
    Devuelve la cámara con la mayor actividad.
    """
    return max(camaras.values(), key=lambda x: x["actividad"])

# Funciones adicionales para controlar características de las cámaras
def cambiar_vision(id_camara):
    if camaras[id_camara]["estado"] == "ON":
        hora_actual = datetime.now().hour
        if 18 <= hora_actual or hora_actual < 6:
            if not camaras[id_camara]["vision_nocturna"]:
                camaras[id_camara]["vision_nocturna"] = True
                registrar_evento(id_camara, "Cambiando a visión nocturna.")
        else:
            if camaras[id_camara]["vision_nocturna"]:
                camaras[id_camara]["vision_nocturna"] = False
                registrar_evento(id_camara, "Cambiando a visión diurna.")

def detectar_movimiento(id_camara):
    if camaras[id_camara]["estado"] == "ON":
        movimiento_detectado = True
        if movimiento_detectado:
            registrar_evento(id_camara, "Movimiento detectado.")
            enviar_alerta(id_camara)

def enviar_alerta(id_camara):
    print(f"Alerta: Movimiento detectado por la cámara {id_camara}!")

def rotar_camara(id_camara, direccion):
    if camaras[id_camara]["estado"] == "ON":
        direcciones = ["izquierda", "derecha", "arriba", "abajo"]
        if direccion in direcciones:
            registrar_evento(id_camara, f"Rotando cámara hacia {direccion}.")
    else:
        print("La cámara está apagada y no puede rotar.")

def registrar_evento(id_camara, descripcion):
    evento = {
        "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "descripcion": descripcion
    }
    camaras[id_camara]["registro_eventos"].append(evento)
    print(f"{evento['hora']}: {evento['descripcion']}")

def mostrar_registro(id_camara):
    print(f"\nHistorial de eventos para la cámara {id_camara}:")
    for evento in camaras[id_camara]["registro_eventos"]:
        print(f"{evento['hora']}: {evento['descripcion']}")
