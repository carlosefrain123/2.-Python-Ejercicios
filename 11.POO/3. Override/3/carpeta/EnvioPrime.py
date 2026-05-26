from carpeta.Envio import Envio
class EnvioPrime(Envio):
    def __init__(self, destino):
        self.destino=destino
    def calcular_costo(self):
        self.calcular_costo="free"
        print(f"⚡ Envío Prime a {self.destino}: GRATIS 🎉")