from carpetas.Dispositivo import Dispositivo
class iPhone(Dispositivo):
    def __init__(self, modelo, precio,almacenamiento,color):
        super().__init__(modelo, precio)
        self.almacenamiento=almacenamiento
        self.color=color
    def presentar(self):
        print(f"Modelo: {self.modelo} | Precio: {self.precio}")
        print(f"Almacenamiento: {self.almacenamiento} | Color: {self.color} ")