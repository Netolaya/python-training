
## crear cuestionario
## actualizar un cuestionario
## eliminar cuestionario
from utils import opcion_invalida, existe_cuestionario
import json
print("[1]: Crear Cuestionario")
print("[2]: Actualizar Cuestionario")
print("[3]: Eliminar Cuestionario")

opcion = input("Ingrese una opcion: ")

## crear

if opcion == "1":

    nombre_cuestionario = input("Ingrese el nombre de cuestionario: ")
    if existe_cuestionario(nombre_cuestionario):
        print(f"El cuestionario {nombre_cuestionario} ya existe, solo se puede actualizar")
    else:
        ## datos de las preguntas
        continuar=True
        data = []
        while continuar:
            pregunta = input("Ingrese la pregunta: ")
            continuar = True
            while continuar:
                opciones = input("Ingrese las opciones separados por comas: ")
                opciones = opciones.split(",")
                if len(opciones) > 1:
                    continuar = False
                else:
                    print("Debes colocar mas de una opcion")
            for idx, opcion in enumerate(opciones):
                print(f"[{idx+1}] {opcion}")
            continuar = True
            while continuar:
                respuesta = input("Ingrese la opcion de la respuesta correcta: ")
                if not opcion_invalida(respuesta, opciones):
                    continuar = False
            
            ## pregunta
            dict_pregunta = {
                "pregunta": pregunta,
                "opciones": opciones,
                "respuesta": respuesta
            }
            data.append(dict_pregunta)
            continuar= input("Desea agregar mas preguntas?: (S/N)").upper() == "S"

        data = json.dumps(data, indent=4)

        ## crear cuestionario
        archivo_cuestionario = open(f"{nombre_cuestionario}.json", "w")
        archivo_cuestionario.write(data)
        archivo_cuestionario.close()
        
        ### 
        #data = [nombre_cuestionario]
        
        cuestionarios = open("cuestionarios.json","r")
        data = json.load(cuestionarios)
        cuestionarios.close()
        
        cuestionarios = open("cuestionarios.json", "w")
        data.append(nombre_cuestionario)
        data = json.dumps(data, indent=4)
        cuestionarios.write(data)
        cuestionarios.close()


    