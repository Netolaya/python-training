
## crear cuestionario
## actualizar un cuestionario
## eliminar cuestionario
from archivos import escribir_archivo, abrir_archivo
from utils import opcion_invalida, existe_cuestionario
from os import remove
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

        #data = json.dumps(data, indent=4)

        ## crear cuestionario
        escribir_archivo(f"{nombre_cuestionario}.json", data)
        
        data = abrir_archivo("cuestionarios.json")
        data.append(nombre_cuestionario)

        escribir_archivo("cuestionarios.json",data)
elif opcion == "2":
    ## actualizar cuestionario
    nombre_cuestionario = input("Que cuestionario desea actualizar: ")
    # validacion
    archivo = open(f'{nombre_cuestionario}.json', 'r')
    data = json.load(archivo)
    archivo.close()
    #print(data)
    print("[1]: Añadir pregunta")
    print("[2]: Eliminar pregunta")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        ## codigo
        continuar = True
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
        
        escribir_archivo(f'{nombre_cuestionario}.json',data)

    elif opcion == 2:
        for idx, pregunta in enumerate(data):
            print(f"[{idx+1}] {pregunta.get('pregunta')}")
        
        numero_pregunta = int(input("Ingrese la opcion que desea eliminar: "))
        nuevas_preguntas = []
        for idx, pregunta in enumerate(data):
            if ((idx + 1) != numero_pregunta):
                nuevas_preguntas.append(pregunta)
        
        escribir_archivo(f'{nombre_cuestionario}.json',data)

elif opcion == "3":
    nombre_archivo = input("Ingrese el nombre del cuestionario que desea eliminar: ")
    remove(f'{nombre_archivo}.json')
    data = abrir_archivo("cuestionarios.json")
    
    def nuevos_cuestionarios(nombre):
        if nombre != nombre_archivo:
            return True
        return False
    
    nueva_data = list(filter(nuevos_cuestionarios, data))
    escribir_archivo("cuestionarios.json",nueva_data)
   
    
    
    


    