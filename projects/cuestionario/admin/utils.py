def opcion_invalida(respuesta, opciones):
    try:
        if int(respuesta) in range(1,len(opciones)+1):
            return False
        else:
            print(f"{respuesta} no es una opcion valida")
            return True
    except:
        print(f"{respuesta} no es una opcion valida")
        return True