class Sobreviviente:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def info(self):
        print(f"👤 Nombre: {self.nombre} | Edad: {self.edad} años")