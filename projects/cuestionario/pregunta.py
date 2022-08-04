
class Clase_Pregunta():
    ## inicializar
    def __init__(self, nombre_pregunta, opciones, opcion_correcta):
        self.nombre_pregunta = nombre_pregunta
        self.opciones = opciones
        self.opcion_correcta = opcion_correcta

    def mostrar_pregunta(self):
        print(self.nombre_pregunta)
        for indice, opcion in enumerate(self.opciones):
            print(f"{indice+1}: {opcion}")
    
    def es_correcta(self, respuesta):
        if respuesta == self.opcion_correcta:
            return True
        else:
            return False

    def opcion_invalida(self, respuesta):
        try:
            if int(respuesta) in range(1,len(self.opciones)+1):
                return False
            else:
                print(f"{respuesta} no es una opcion valida")
                return True
        except:
            print(f"{respuesta} no es una opcion valida")
            return True

        