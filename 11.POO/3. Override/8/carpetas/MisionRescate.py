from carpetas.Mision import Mision
class MisionRescate(Mision):
    def __init__(self,sobreviviente,ubicacion):
        self.sobreviviente=sobreviviente
        self.ubicacion=ubicacion
    def iniciar(self):
        super().iniciar()
        print(f"Sobreviviente: {self.sobreviviente}")
        print(f"Ubicación: {self.ubicacion}")