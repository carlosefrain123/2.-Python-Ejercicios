from Figuras.Figura import Figura
class Cuadrado(Figura):
    def __init__(self,lado):
        super().__init__()
        self.lado=lado
        
    def area(self):
        total=self.lado**2
        print(f"Área del cuadrado es: {total}")