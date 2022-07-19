## crear un programa que te permita ingresar el nombre y 
# la edad de la persona, y almacenarlo en una lista de diccionarios, luego debes filtrar las personas que tengan 
# mas de 18 años 

from itertools import permutations


personas=[]

def agregar_persona(nombre, edad):
    persona={'nombre':nombre,'edad':edad}
    personas.append(persona)

def obtener_mayores(personas):
    return list(filter(lambda x: x.get('edad') > 18, personas))

def obtener_el_mayor(personas):
    mayor_edad=0
    nombre_mayor=""
    for persona in personas:
        edad=persona.get('edad')
        nombre=persona.get('nombre')
        if edad >mayor_edad:
            mayor_edad=edad
            nombre_mayor=nombre
    return {"nombre": nombre_mayor, "edad": mayor_edad}

def obtener_el_menor(personas):
    menor_edad=10000000000
    nombre_menor=""
    for persona in personas:
        edad=persona.get('edad')
        nombre=persona.get('nombre')
        if edad<menor_edad:
            menor_edad=edad
            nombre_menor=nombre
    return {"nombre": nombre_menor, "edad": menor_edad}

def total_edad(personas):
    from functools import reduce
    return reduce(lambda x,y: x+y['edad'],personas,0)


continuar=True
while continuar:
    nombre=input("Ingrese el nombre: ")
    edad=int(input("Ingrese la edad: "))
    agregar_persona(nombre, edad)
    continuar=input("Desea continuar: (SI/NO): ").upper()=="SI"

print(obtener_mayores(personas))
persona_mayor = obtener_el_mayor(personas)
print(f"El mas viejo es {persona_mayor.get('nombre')} y tiene {persona_mayor.get('edad')} años")
persona_menor = obtener_el_menor(personas)
print(f"el mas chibolo es {persona_menor.get('nombre')} y tiene {persona_menor.get('edad')} años")
print(personas)
print("Total: ", total_edad(personas))
