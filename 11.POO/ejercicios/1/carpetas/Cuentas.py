class Cuentas:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
    def info(self):
        print(f"Titular: {self.titular} | Saldo: {self.saldo}")