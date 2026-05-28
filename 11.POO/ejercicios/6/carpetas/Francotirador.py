from carpetas.Combatiente import Combatiente
class Francotirador(Combatiente):
    def __init__(self, nombre, vida,precision):
        super().__init__(nombre, vida)
        self.precision=precision
    def atacar(self):
        super().atacar()
        print(f"🎯 Disparo a distancia con {self.precision}% de precisión")