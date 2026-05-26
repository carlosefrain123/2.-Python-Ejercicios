from carpetas.Canal import Canal
class CanalGaming(Canal):
    def __init__(self, nombre, suscriptores,juego_principal):
        super().__init__(nombre, suscriptores)
        self.juego_principal=juego_principal
    def publicar(self):
        super().publicar()
        print(f"El juego principal es: {self.juego_principal}")