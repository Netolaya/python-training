class Cuadrado():
    ## inicializar el cuadrado
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4   