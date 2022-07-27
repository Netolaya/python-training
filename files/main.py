import json
file_personas = open("personas.json", "r")
personas = json.load(file_personas)
file_personas.close()
nombre = input("ingrese un nombre: ")
dni = input("ingrese dni: ")
persona = {"nombre": nombre, "dni": dni}
personas.append(persona)
nuevo_archivo = open("personas.json", "w")
dumps_personas = json.dumps(personas, indent=4)
nuevo_archivo.write(dumps_personas)
nuevo_archivo.close()
