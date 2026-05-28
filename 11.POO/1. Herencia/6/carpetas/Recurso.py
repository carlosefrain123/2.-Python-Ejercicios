class Recurso:
    def __init__(self,nombre,cantidad):
        self.nombre=nombre
        self.cantidad=cantidad
    def usar(self):
        self.cantidad-=1
        if self.cantidad<0:
            self.cantidad=0
            print(f"El recurso {self.nombre}, ya no tiene recursos")
        else:
            print(f"El recurso {self.nombre}, tiene stock: {self.cantidad}")