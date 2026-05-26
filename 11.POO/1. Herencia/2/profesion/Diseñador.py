from profesion.Empleado import Empleado as e
class Diseñador(e):
    def diseñar(self):
        print(f"El empleado {self.nombre}, está haciendo marketing")