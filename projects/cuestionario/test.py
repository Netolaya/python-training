## Futbol
## Que tanto sabes de Futbol
## 5 preguntas
## Por cada pregunta debe mostrarte las opciones, y con un input para que puedas responder la opcion correcta
## Se debe hacer un calculo para saber si la respuesta es correcta o no

## Datos
pregunta = 'Donde se realizo el primer mundial?'
opciones = [
    "brasil",
    "alemania",
    "uruguay"
]
opcion_correcta = "3"

## Formato de la pregunta
print(pregunta)
for indice, opcion in enumerate(opciones):
    print(f"{indice+1}: {opcion}")

## Escoja opcion
respuesta = input("Escoge la opcion correcta ?: ")

## Verifiques la respuesta 
if respuesta == opcion_correcta:
    print("Respuesta correcta")
else:
    print("Respuesta incorrecta")
