from carpetas.Dispositivo import Dispositivo as disp
class Laptop(disp):
    def __init__(self, marca, bateria, ram):
        super().__init__(marca, bateria)
        self.ram=ram
    def info(self):
        super().info()
        print(f"El ram es: {self.ram}")