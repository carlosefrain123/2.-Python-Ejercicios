class Electrodomestico:
    def __init__(self,marca,precio):
        self.marca=marca
        self.precio=precio
    def encender(self):
        print(f"El electrodometico {self.marca}, está encendido.")
    def apagar(self):
        print(f"El electrodometico {self.marca}, está apagado.")
        