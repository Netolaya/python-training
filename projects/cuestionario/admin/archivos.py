import json

def abrir_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    data = json.load(archivo)
    archivo.close()
    return data

def escribir_archivo(nombre_archivo,data):
    archivo = open(nombre_archivo, "w")
    data = json.dumps(data, indent=4)
    archivo.write(data)
    archivo.close()