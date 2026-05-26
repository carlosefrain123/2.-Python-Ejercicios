class Viaje():
    def __init__(self,origen,destino):
        self.origen=origen
        self.destino=destino
    def calcular_tarifa(self):
        print("Calculando")
    def info(self):
        print(f"Origen: {self.origen} | Destino: {self.destino}")