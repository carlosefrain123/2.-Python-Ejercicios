from carpeta.Bunker import Bunker
class BunkerMovil(Bunker):
    def __init__(self, nombre, capacidad,vehiculo):
        super().__init__(nombre, capacidad)
        self.vehiculo=vehiculo
    def estado(self):
        super().estado()
        print(f"   Vehículo: {self.vehiculo} 🚛")