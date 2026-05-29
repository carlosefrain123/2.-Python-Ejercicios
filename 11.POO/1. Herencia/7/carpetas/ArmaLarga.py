from carpetas.Arma import Arma
class ArmaLarga(Arma):
    def ataque_rapido(self):
        print(f"{self.nombre} disparo de precisión! Daño: {self.daño}")
    