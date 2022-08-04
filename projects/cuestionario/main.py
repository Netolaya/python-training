import json
from urllib import response
from pregunta import Clase_Pregunta
## Leer el archivo de preguntas
archivo_preguntas = open("preguntas.json", "r")
preguntas = json.load(archivo_preguntas)
cuestionario = []
## armando el cuestionario
for pregunta in preguntas:
    nueva_pregunta = Clase_Pregunta(pregunta.get('pregunta'), pregunta.get('opciones'), pregunta.get('respuesta'))    
    cuestionario.append(nueva_pregunta)

puntaje = 0
## recorrer el questionario
for pregunta in cuestionario:
    pregunta.mostrar_pregunta()
    opcion_invalida = True
    while opcion_invalida:
        respuesta = input("Escoge la opcion correcta ?: ")
        opcion_invalida = pregunta.opcion_invalida(respuesta)
    if pregunta.es_correcta(respuesta):
        puntaje += 1

print(f"tu puntaje es {puntaje}")