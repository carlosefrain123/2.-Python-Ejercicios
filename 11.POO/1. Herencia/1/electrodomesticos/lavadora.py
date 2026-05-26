from electrodomesticos.electrodomestico import Electrodomestico as e
class Lavadora(e):
    def lavar(self):
        print(f"La marca {self.marca}, está lavando")
    