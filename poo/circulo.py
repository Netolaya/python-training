class Circulo():
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self.radio * self.radio * math.pi
    
    def perimetro(self):
        return 2 * math.pi * self.radio