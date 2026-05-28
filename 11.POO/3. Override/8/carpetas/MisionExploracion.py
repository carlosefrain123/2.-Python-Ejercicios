from carpetas.Mision import Mision
class MisionExploracion(Mision):
    def __init__(self,zona,riesgo):
        self.zona=zona
        self.riesgo=riesgo
    def iniciar(self):
        super().iniciar()
        print(f"Zona: {self.zona}")
        print(f"Riesgo: {self.riesgo}")