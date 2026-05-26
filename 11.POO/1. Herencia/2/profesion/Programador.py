from profesion.Empleado import Empleado as e
class Programador(e):
    def codear(self):
        print(f"El empleado {self.nombre}, está codeando.")