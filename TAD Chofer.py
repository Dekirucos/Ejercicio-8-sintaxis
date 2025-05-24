def crearChofer():
    return {
        "nombre": "",
        "apellido": "",
        "legajo": 0,
        "fecha_ingreso": "",
        "numero_camion": "",
        "zona_trabajo": ""
    }

def cargarChofer(chofer, nombre, apellido, legajo, fecha_ingreso, numero_camion, zona_trabajo):
    chofer["nombre"] = nombre
    chofer["apellido"] = apellido
    chofer["legajo"] = legajo
    chofer["fecha_ingreso"] = fecha_ingreso
    chofer["numero_camion"] = numero_camion
    chofer["zona_trabajo"] = zona_trabajo

def verNombre(chofer):
    return chofer["nombre"]

def verApellido(chofer):
    return chofer["apellido"]

def verLegajo(chofer):
    return chofer["legajo"]

def verFechaIngreso(chofer):
    return chofer["fecha_ingreso"]

def verNumeroCamion(chofer):
    return chofer["numero_camion"]

def verZonaTrabajo(chofer):
    return chofer["zona_trabajo"]

def modificarChofer(chofer):
    nombre = input("Nuevo nombre (Enter para mantener): ")
    apellido = input("Nuevo apellido (Enter para mantener): ")
    fecha_ingreso = input("Nueva fecha de ingreso (AAAA-MM-DD) (Enter para mantener): ")
    numero_camion = input("Nuevo número de camión (Enter para mantener): ")
    zona = input("Nueva zona de trabajo (Enter para mantener): ")

    if nombre == "":
        nombre = verNombre(chofer)
    if apellido == "":
        apellido = verApellido(chofer)
    if fecha_ingreso == "":
        fecha_ingreso = verFechaIngreso(chofer)
    if numero_camion == "":
        numero_camion = verNumeroCamion(chofer)
    if zona == "":
        zona = verZonaTrabajo(chofer)

    cargarChofer(chofer, nombre, apellido, verLegajo(chofer), fecha_ingreso, numero_camion, zona)
