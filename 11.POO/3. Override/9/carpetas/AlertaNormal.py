from carpetas.Alerta import Alerta
class AlertaNormal(Alerta):
    def __init__(self,zona,descripcion):
        self.zona=zona
        self.descripcion=descripcion
    def activar(self):
        super().activar()
        print("--- ALERTA NORMAL ---")
        print(f"Zona: {self.zona}")
        print(f"Descripción: {self.descripcion}")
        print("👉 Monitorear la situación")
        