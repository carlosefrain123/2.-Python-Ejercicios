from carpetas.Arma import Arma
class ArmaCorta(Arma):
    def ataque_rapido(self):
        print(f"{self.nombre} ataque rápido! Daño: {self.daño}")
    