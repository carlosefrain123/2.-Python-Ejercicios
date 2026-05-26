from carpeta.Envio import Envio
class EnvioEstandar(Envio):
    def __init__(self,peso):
        self.peso = peso

    def calcular_costo(self):
        print(f"📦 Envío estándar ({self.peso}kg): S/15")