## crear una clase "Cuadrado" que tenga como argumento el lado, 
## obtener el perimetro y el area del cuadrado

class Cuadrado():
    ## inicializar el cuadrado
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4



continuar = True
while continuar:
    lado = int(input("Ingrese el lado del cuadrado: "))
    c = Cuadrado(lado)
    print(f"Area: {c.area()}")
    print(f"Perimetro: {c.perimetro()}")
    continuar = input("Desea continuar (S/N)").upper() == "S"