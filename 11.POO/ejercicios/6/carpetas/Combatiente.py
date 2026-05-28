class Combatiente:
    def __init__(self,nombre,vida):
        self.nombre=nombre
        self.vida=vida
    def atacar(self):
        print("Atacando...")
    def info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        