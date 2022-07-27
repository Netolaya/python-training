import json
dni = input("Ingrese el dni que desea eliminar?: ")
file_personas = open("personas.json", "r")
personas = json.load(file_personas)
file_personas.close()


