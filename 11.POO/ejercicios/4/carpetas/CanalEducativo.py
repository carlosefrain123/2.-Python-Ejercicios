from carpetas.Canal import Canal
class CanalEducativo(Canal):
    def __init__(self, nombre, suscriptores,tema):
        super().__init__(nombre, suscriptores)
        self.tema=tema
    def publicar(self):
        super().publicar()
        print(f"📚 Nueva lección de {self.tema} disponible!")