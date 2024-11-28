# Diccionario 
camaras = {}

# Lista  eventos 
eventos = []

# Funcion para agregar una nueva camara
def agregar_camara(camaras):
    print("\nSeleccione una ubicacion para la camara [numero]:")
    ubicaciones_validas = ["Hospital", "Plaza", "Policia", "Municipio", "Parque", "Escuela", "Universidad", "Calle"]
    for idx, ubicacion in enumerate(ubicaciones_validas, 1):
        print(f"{idx}. {ubicacion}")

    ubicacion = ""
    while not ubicacion:
        seleccion = input("Seleccione el numero correspondiente a la ubicacion: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(ubicaciones_validas):
            ubicacion = ubicaciones_validas[int(seleccion) - 1]
        else:
            print("Seleccion no valida. Intente de nuevo.")

    if ubicacion == "Calle":
        calle = ""
        while not calle.isdigit():
            calle = input("Ingrese el numero de la calle: ")
            if not calle.isdigit():
                print("Debe ingresar un numero valido para la calle.")
    else:
        calle = None

    camara_id = ""
    while not camara_id:
        camara_id = input("Ingrese el ID de la camara [Solo numeros]: ")
        if not camara_id.isdigit():
            print("El ID debe ser numerico.")
            camara_id = ""
        elif f"#{camara_id}" in camaras:
            print("Este ID ya existe. Intente con otro.")
            camara_id = ""
    
    camara_id = f"#{camara_id}"
    camaras[camara_id] = {
        'ubicacion': ubicacion,
        'calle': calle,
        'estado': 'apagada'
    }
    print(f"Camara {camara_id} agregada en {ubicacion}{' - Calle ' + calle if calle else ''}.")

# Funcion para listar todas las camaras
def listar_camaras(camaras):
    if not camaras:
        print("\nNo hay camaras disponibles.")
        return

    ubicaciones = agrupar_camaras_por_ubicacion(camaras)
    mostrar_camaras_por_ubicacion(ubicaciones)

# Funcion para agrupar camaras por ubicacion
def agrupar_camaras_por_ubicacion(camaras):
    ubicaciones = {}
    for camara_id, camara_info in camaras.items():
        ubicacion = camara_info['ubicacion']
        if ubicacion not in ubicaciones:
            ubicaciones[ubicacion] = []
        ubicaciones[ubicacion].append({**camara_info, 'id': camara_id})
    return ubicaciones

# Funcion para mostrar las camaras por ubicacion
def mostrar_camaras_por_ubicacion(ubicaciones):
    for ubicacion, camaras_ubicacion in ubicaciones.items():
        print(f"\n[Ubicacion]: {ubicacion}")
        if ubicacion == "Calle":
            calles = {}
            for camara in camaras_ubicacion:
                calle = camara['calle']
                if calle not in calles:
                    calles[calle] = []
                calles[calle].append(camara)
            for calle, camaras_calle in calles.items():
                print(f"  Calle {calle}:")
                for camara in camaras_calle:
                    print(f"    ID: {camara['id']} - Estado: {camara['estado']}")
        else:
            print("[Camaras]")
            for camara in camaras_ubicacion:
                print(f"  ID: {camara['id']} - Estado: {camara['estado']}")

# Funcion para modificar la configuracion de camaras (agregar o eliminar)
def modificar_configuracion(camaras):
    print("\nSubmenu de Configuracion de Camaras")
    print("1. Agregar camara")
    print("2. Eliminar camara")
    print("0. Volver al menu principal")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_camara(camaras)
    elif opcion == "2":
        eliminar_camara(camaras)
    elif opcion == "0":
        return
    else:
        print("Opcion no valida.")

# Funcion para eliminar una camara
def eliminar_camara(camaras):
    # Mostrar las ubicaciones activas
    print("\n[Ubicaciones activas]")
    ubicaciones_activas = {ubicacion: [] for ubicacion in ["Hospital", "Plaza", "Policia", "Municipio", "Parque", "Escuela", "Universidad", "Calle"]}
    
    # Filtrar ubicaciones con camaras activas
    for camara_id, camara_info in camaras.items():
        ubicacion = camara_info['ubicacion']
        if camara_info['estado'] != 'apagada':
            ubicaciones_activas[ubicacion].append(camara_id)

    ubicaciones_con_camaras = {ubicacion: cams for ubicacion, cams in ubicaciones_activas.items() if cams}
    
    if not ubicaciones_con_camaras:
        print("No hay camaras activas para eliminar.")
        return
    
    # Mostrar las ubicaciones con camaras activas
    for idx, ubicacion in enumerate(ubicaciones_con_camaras, 1):
        print(f"{idx}. {ubicacion}")

    # Solicitar al usuario que seleccione una ubicacion
    ubicacion_seleccionada = ""
    while not ubicacion_seleccionada:
        seleccion = input("Seleccione el numero correspondiente a la ubicacion para consultar las camaras: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(ubicaciones_con_camaras):
            ubicacion_seleccionada = list(ubicaciones_con_camaras.keys())[int(seleccion) - 1]
        else:
            print("Seleccion no valida. Intente de nuevo.")
    
    # Mostrar las camaras activas en la ubicacion seleccionada
    print(f"\nCamaras activas en {ubicacion_seleccionada}:")
    for camara_id in ubicaciones_con_camaras[ubicacion_seleccionada]:
        print(f"  ID: {camara_id} - Estado: {camaras[camara_id]['estado']}")
    
    # Solicitar el ID de la camara a eliminar
    camara_id = input("\nIngrese el ID de la camara a eliminar (formato #ID): ")
    if camara_id in camaras:
        del camaras[camara_id]
        print(f"Camara {camara_id} eliminada.")
    else:
        print("ID de camara no encontrado.")

# Funcion para manejar encendido y apagado de camaras
def manejar_camara(camaras, estado_deseado):
    print(f"\nSeleccione la camara que desea {estado_deseado}:")
    if not camaras:
        print("No hay camaras disponibles.")
        print("¿Quieres agregar una camara? Puedes hacerlo seleccionando la opcion 1.")
        return

    listar_camaras(camaras)

    camara_id = input("Ingrese el ID de la camara (formato #ID): ")
    if camara_id in camaras:
        if camaras[camara_id]['estado'] == estado_deseado:
            print(f"La camara {camara_id} ya esta {estado_deseado}.")
        else:
            camaras[camara_id]['estado'] = estado_deseado
            print(f"Camara {camara_id} {estado_deseado}.")
            eventos.append({'id': camara_id, 'estado': estado_deseado})
    else:
        print("ID de camara no encontrado.")

# Funcion para consultar el estado de una camara
# Funcion para consultar el estado de una camara
def consultar_estado(camaras):
    # Mostrar las ubicaciones activas
    print("\n[Ubicaciones activas]")
    ubicaciones_activas = {ubicacion: [] for ubicacion in ["Hospital", "Plaza", "Policia", "Municipio", "Parque", "Escuela", "Universidad", "Calle"]}
    
    # Filtrar ubicaciones con camaras activas
    for camara_id, camara_info in camaras.items():
        ubicacion = camara_info['ubicacion']
        if camara_info['estado'] != 'apagada':
            ubicaciones_activas[ubicacion].append(camara_id)

    ubicaciones_con_camaras = {ubicacion: cams for ubicacion, cams in ubicaciones_activas.items() if cams}
    
    if not ubicaciones_con_camaras:
        print("No hay camaras activas para consultar.")
        return
    
    # Mostrar las ubicaciones con camaras activas
    for idx, ubicacion in enumerate(ubicaciones_con_camaras, 1):
        print(f"{idx}. {ubicacion}")

    # Solicitar al usuario que seleccione una ubicacion
    ubicacion_seleccionada = ""
    while not ubicacion_seleccionada:
        seleccion = input("Seleccione el numero correspondiente a la ubicacion para consultar las camaras: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(ubicaciones_con_camaras):
            ubicacion_seleccionada = list(ubicaciones_con_camaras.keys())[int(seleccion) - 1]
        else:
            print("Seleccion no valida. Intente de nuevo.")
    
    # Mostrar las camaras activas en la ubicacion seleccionada
    print(f"\nCamaras activas en {ubicacion_seleccionada}:")
    for camara_id in ubicaciones_con_camaras[ubicacion_seleccionada]:
        print(f"  ID: {camara_id} - Estado: {camaras[camara_id]['estado']}")
    
    # Solicitar el ID de la camara a consultar
    camara_id = input("\nIngrese el ID de la camara a consultar (formato #ID): ")
    if camara_id in camaras:
        print(f"Estado de la camara {camara_id}: {camaras[camara_id]['estado']}")
    else:
        print("ID de camara no encontrado.")


# Funcion para generar un reporte diario
def reporte_diario(eventos):
    if not eventos:
        print("\nNo hay eventos registrados hoy.")
        return
    print("\n[Reporte Diario]")
    for evento in eventos:
        print(f"Camara {evento['id']} - Estado: {evento['estado']}")

# Funcion para generar un reporte completo de camaras
def generar_reporte(camaras):
    print("\n[Reporte Completo]")
    listar_camaras(camaras)

# Funcion para capturar un evento en una camara
def capturar_evento(camaras, eventos):
    # Filtrar las ubicaciones activas con camaras encendidas
    ubicaciones_activas = {ubicacion: [] for ubicacion in ["Hospital", "Plaza", "Policia", "Municipio", "Parque", "Escuela", "Universidad", "Calle"]}
    
    for camara_id, camara_info in camaras.items():
        if camara_info['estado'] != 'apagada':
            ubicaciones_activas[camara_info['ubicacion']].append(camara_id)

    # Filtrar ubicaciones con camaras activas
    ubicaciones_con_camaras = {ubicacion: cams for ubicacion, cams in ubicaciones_activas.items() if cams}
    
    if not ubicaciones_con_camaras:
        print("No hay camaras activas para capturar eventos.")
        return

    # Mostrar las ubicaciones con camaras activas
    print("\nUbicaciones activas con camaras encendidas:")
    for idx, ubicacion in enumerate(ubicaciones_con_camaras, 1):
        print(f"{idx}. {ubicacion}")
    
    # Solicitar al usuario que seleccione una ubicacion
    ubicacion_seleccionada = ""
    while not ubicacion_seleccionada:
        seleccion = input("Seleccione el numero correspondiente a la ubicacion: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(ubicaciones_con_camaras):
            ubicacion_seleccionada = list(ubicaciones_con_camaras.keys())[int(seleccion) - 1]
        else:
            print("Seleccion no valida. Intente de nuevo.")
    
    # Mostrar las camaras activas en la ubicacion seleccionada
    print(f"\nCamaras activas en {ubicacion_seleccionada}:")
    for camara_id in ubicaciones_con_camaras[ubicacion_seleccionada]:
        print(f"  ID: {camara_id} - Estado: {camaras[camara_id]['estado']}")
    
    # Solicitar el ID de la camara donde capturar el evento
    camara_id = input("\nIngrese el ID de la camara donde desea capturar un evento (formato #ID): ")
    if camara_id in camaras and camaras[camara_id]['estado'] != 'apagada':
        # Solicitar el tipo de evento 
        tipo_evento = input("Ingrese el tipo de evento: ")
        
        # capturar un evento y agregarlo a la lista de eventos
        evento = {
            'id': camara_id,
            'estado': camaras[camara_id]['estado'],
            'tipo': tipo_evento
        }
        eventos.append(evento)
        print(f"Evento capturado en la camara {camara_id}: {tipo_evento}")
    else:
        print("ID de camara no encontrado o la camara esta apagada.")

# menu
def mostrar_menu():
    while True:
        print("\nSistema de Gestion de Camaras")
        print("1. Agregar o quitar una camara")
        print("2. Encender camara")
        print("3. Apagar camara")
        print("4. Consultar estado de camara")
        print("5. Capturar evento en camara")
        print("6. Listar camaras")
        print("7. Generar reporte diario")
        print("8. Mostrar reporte diario")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            modificar_configuracion(camaras)
        elif opcion == "2":
            manejar_camara(camaras, "encendida")
        elif opcion == "3":
            manejar_camara(camaras, "apagada")
        elif opcion == "4":
            consultar_estado(camaras)
        elif opcion == "5":
            capturar_evento(camaras, eventos)
        elif opcion == "6":
            listar_camaras(camaras)
        elif opcion == "7":
            reporte_diario(eventos)
        elif opcion == "8":
            generar_reporte(camaras)
        elif opcion == "0":
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    mostrar_menu()
    