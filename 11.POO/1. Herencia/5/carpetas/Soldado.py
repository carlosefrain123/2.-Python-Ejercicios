from carpetas.Sobreviviente import Sobreviviente
class Soldado(Sobreviviente):
    def disparar(self):
        print(f"El soldado {self.nombre}, está disparando.")