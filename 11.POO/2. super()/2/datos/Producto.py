class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    def mostrar(self):
        print(f"{self.nombre}: S/{self.precio}")