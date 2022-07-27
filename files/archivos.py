import json
def abrir_archivo(nombre):
    file = open(nombre, "r")
    data = json.load(file)
    file.close()
    return data

def escribir_archivo(nombre, data):
    archivo = open(nombre, "w")
    data = json.dumps(data, indent=4)
    archivo.write(data)
    archivo.close()