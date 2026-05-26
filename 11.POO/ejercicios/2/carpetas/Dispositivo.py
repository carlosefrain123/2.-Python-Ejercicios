class Dispositivo():
    def __init__(self,marca,bateria):
        self.marca=marca
        self.bateria=bateria
    def cargar(self):
        self.bateria+=20
        if self.bateria>=100:
            self.bateria=100
        print(f"{self.marca} cargando, batería: {self.bateria}%")
    def info(self):
        print(f"Marca: {self.marca} | Batería: {self.bateria}%")
