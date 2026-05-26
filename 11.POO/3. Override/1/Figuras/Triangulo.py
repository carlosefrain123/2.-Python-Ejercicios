from Figuras.Figura import Figura
class Triangulo(Figura):
    def __init__(self,base,altura):
        super().__init__()
        self.base=base
        self.altura=altura
    def area(self):
        resultado=(self.base*self.altura)/2
        print(f"El área del triángulo es: {resultado}")
        