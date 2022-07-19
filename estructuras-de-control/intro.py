
nombres = ['raul', 'helen', 'yeli', 'neto']
personas = [{'nombre': 'raul', 'edad': 23},{'nombre': 'neto', 'edad': 28},{'nombre': 'helen', 'edad': 56},{'nombre': 'yeli', 'edad': 28}]

#for nombre in nombres:
#    print(nombre)

suma = 0
contador = 0
for persona in personas:
    contador = contador + 1
    suma = suma + persona.get('edad')
    #print(persona.get('edad'))
promedio = suma / len(personas)
#print(promedio)
#print(suma)

frase = "hola mundo"
for letra in frase:
    print(letra)

