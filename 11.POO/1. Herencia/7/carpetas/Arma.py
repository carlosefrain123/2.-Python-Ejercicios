class Arma:
    def __init__(self,nombre,daño):
        self.nombre=nombre
        self.daño=daño
    def equipar(self):
        print(f"{self.nombre} equipada ⚔️")
    def guardar(self):
        print(f"{self.nombre} guardada en el inventario 🎒")
    