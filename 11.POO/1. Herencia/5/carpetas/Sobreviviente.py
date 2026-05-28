class Sobreviviente:
    def __init__(self,nombre,vida):
        self.nombre=nombre
        self.vida=vida
    def descansar(self):
        self.vida+=20
        if self.vida>=100:
            self.vida=100
        print(f"La vida está: {self.vida}")

