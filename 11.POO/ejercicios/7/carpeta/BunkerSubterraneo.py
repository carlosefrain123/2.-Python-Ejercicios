from carpeta.Bunker import Bunker
class BunkerSubterraneo(Bunker):
    def __init__(self, nombre, capacidad,nivel_subterraneo):
        super().__init__(nombre, capacidad)
        self.nivel_subterraneo=nivel_subterraneo
    def estado(self):
        super().estado()
        print(f"   Nivel  : {self.nivel_subterraneo} metros bajo tierra 🪨")