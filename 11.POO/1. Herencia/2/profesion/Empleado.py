class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre=nombre
        self.sueldo=sueldo
    def trabajar(self):
        print(f"El trabajador {self.nombre}, está chambeando.")