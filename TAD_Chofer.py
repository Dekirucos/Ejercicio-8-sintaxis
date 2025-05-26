def crearChofer():
    return ["", "", 0, "", "", ""]

def cargarChofer(chofer, nombre, apellido, legajo, fecha_ingreso, numero_camion, zona_trabajo):
    chofer[0] = nombre
    chofer[1] = apellido
    chofer[2] = legajo
    chofer[3] = fecha_ingreso
    chofer[4] = numero_camion
    chofer[5] = zona_trabajo


def verNombre(chofer): return chofer[0]
def verApellido(chofer): return chofer[1]
def verLegajo(chofer): return chofer[2]
def verFechaIngreso(chofer): return chofer[3]
def verNumeroCamion(chofer): return chofer[4]
def verZonaTrabajo(chofer): return chofer[5]

def modNombre(chofer, nuevo): chofer[0] = nuevo
def modApellido(chofer, nuevo): chofer[1] = nuevo
def modLegajo(chofer, nuevo): chofer[2] = nuevo
def modFechaIngreso(chofer, nuevo): chofer[3] = nuevo
def modNumeroCamion(chofer, nuevo): chofer[4] = nuevo
def modZonaTrabajo(chofer, nuevo): chofer[5] = nuevo

#Creo que esta Listo 
