class Rectangulo():
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
    
    def area(self):
        return self.largo*self.ancho 
    
    def perimetro(self):
        return self.largo*2 + self.ancho*2