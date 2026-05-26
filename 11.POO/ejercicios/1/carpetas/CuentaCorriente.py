from carpetas.Cuentas import Cuentas
class CuCo(Cuentas):
    def __init__(self, titular, saldo,interes):
        super().__init__(titular, saldo)
        self.interes=interes
    def info(self):
        super().info()
        print(f"El interes es: {self.interes}%")