from carpetas.Viaje import Viaje
class UberBlack(Viaje):
    def __init__(self, origen, destino,precio_base):
        super().__init__(origen, destino)
        self.precio_base=precio_base
    def calcular_tarifa(self):
        super().info()
        print(f"🚙 UberBlack premium: S/{self.precio_base}")
    