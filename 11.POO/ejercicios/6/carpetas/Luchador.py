from carpetas.Combatiente import Combatiente
class Luchador(Combatiente):
    def __init__(self, nombre, vida,fuerza):
        super().__init__(nombre, vida)
        self.fuerza=fuerza
    def atacar(self):
        super().atacar()
        print(f"👊 Golpe cuerpo a cuerpo con {self.fuerza} de fuerza")