import json
import re
def opcion_invalida(respuesta, opciones):
    try:
        if int(respuesta) in range(1,len(opciones)+1):
            return False
        else:
            print(f"{respuesta} no es una opcion valida")
            return True
    except:
        print(f"{respuesta} no es una opcion valida")
        return True

def existe_cuestionario(nombre_cuestionario):
    archivo = open("cuestionarios.json", "r")
    data = json.load(archivo)
    if nombre_cuestionario in data:
        return True
    return False