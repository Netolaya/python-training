from archivos import abrir_archivo, escribir_archivo

personas = abrir_archivo("personas.json")
nombre = input("ingrese un nombre: ")
dni = input("ingrese dni: ")
persona = {"nombre": nombre, "dni": dni}
personas.append(persona)
escribir_archivo("personas.json", personas)

