from electrodomesticos.electrodomestico import Electrodomestico as e
class Refrigeradora(e):
    def enfriar(self):
        print(f"La marca {self.marca}, está enfriando.")