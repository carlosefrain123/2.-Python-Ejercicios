class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def datos_basicos(self):
        print(f"Nombre: {self.nombre} | Edad: {self.edad}")