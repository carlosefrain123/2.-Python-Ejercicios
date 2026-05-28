from carpetas.Recurso import Recurso
class Comida(Recurso):
    def cocinar(self):
        print(f"🍲 Cocinando {self.nombre} para el equipo")