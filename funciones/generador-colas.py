## El usuario va ingresar los nombres 
## de personas separados por comas, esto se debe almacenar en 
## una lista.. Y luego se debe crear un generador mostrando 
## los nombres de la persona.

lista_nombres=[]
nombres=input("ingrese los nombres separados por ',': ")
lista_nombres=nombres.split(",")
def generador(lista):
    for n in lista:
        yield n
siguiente=generador(lista_nombres)
continuar=True
while continuar:        
    continuar=input("Desea saber el siguiente en la lista? (SI/NO): ").upper()=="SI"
    if continuar:
        try:
            print(next(siguiente))
        except:
            print("Ya no hay mas datos en la cola")
            continuar = False
