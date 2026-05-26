from carpetas.Cuentas import Cuentas
class CuAh(Cuentas):
    def __init__(self, titular, saldo,limite_credito):
        super().__init__(titular, saldo)
        self.limite_credito=limite_credito
    def info(self):
        super().info()
        print(f"El límite creditos es: {self.limite_credito}")