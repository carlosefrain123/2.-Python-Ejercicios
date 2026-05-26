class Dispositivo():
    def __init__(self,modelo,precio):
        self.modelo=modelo
        self.precio=precio
    def info(self):
        print(f"Modelo: {self.modelo} | Precio: {self.precio}")