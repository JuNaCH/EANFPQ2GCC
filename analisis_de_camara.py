# analisis_de_camaras.py

def detectar_movimiento(camara):
    if camara["configuracion"]["deteccion_movimiento"]:
        # detectar movimiento
        return True
    return False

def generar_alerta(camara):
    # generar una alerta
    return f"Alerta generada para la camara en {camara['ubicacion']}"

def obtener_camaras_con_alertas_activas(camaras):
    return [cam for cam in camaras.values() if cam["estado"] == "alerta"]

def contar_eventos_por_tipo(camaras, tipo_evento):
    # eventos segun el tipo
    pass

def calcular_promedio_alertas_por_dia(camaras, dias):
    total_alertas = sum(cam["actividad"] for cam in camaras.values())
    return total_alertas / dias

def obtener_camara_con_menor_actividad(camaras):
    return min(camaras.values(), key=lambda x: x["actividad"])
