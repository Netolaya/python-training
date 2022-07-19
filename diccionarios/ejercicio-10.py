print("GESTION DE CLIENTES")
print("===================")

continuar = True
clientes = {}
while continuar:
    print("(1) Añadir cliente")
    print("(2) Eliminar cliente")
    print("(3) Mostrar cliente")
    print("(4) Listar todos los cliente")
    print("(5) Listas clientes preferentes")
    print("(6) Terminar")

    opcion = input("Escribe una opcion: ")
    if opcion == "1":
        dni = input("Ingrese dni: ")
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese telefono: ")
        preferente = input("Es preferente? (SI/NO): ")
        clientes[dni] = {
            "nombre": nombre,
            "telefono": telefono,
            "preferente": preferente.upper()
        }
    elif opcion == "2":
        dni = input("Ingrese dni: ")
        if dni not in clientes:
            print(f"No existe cliente con dni {dni}")
            continue
        del clientes[dni]
    elif opcion == "3":
        dni = input("Ingrese dni")
        if dni not in clientes:
            print(f"No existe cliente con dni {dni}")
            continue
        print(clientes[dni])
    elif opcion == "4":
        print(clientes)
    elif opcion == "5":
        dnis = clientes.keys()
        for dni in dnis:
            es_preferente = clientes[dni].get("preferente")
            if es_preferente == "SI":
                print(clientes[dni])
    elif opcion == "6":
        print("Termino el programa vete a la michi")
        continuar = False
    else:
        print("Opcion equivocada")
    