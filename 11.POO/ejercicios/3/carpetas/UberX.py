from carpetas.Viaje import Viaje
class UberX(Viaje):
    def __init__(self, origen, destino,pasajero):
        super().__init__(origen, destino)
        self.pasajero=pasajero
    def calcular_tarifa(self):
        super().info()
        tarifa=5*self.pasajero
        print(f"UberX para {self.pasajero} pasajeros: S/{tarifa}")