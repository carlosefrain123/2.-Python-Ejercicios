from carpetas.Alerta import Alerta
class AlertaEmergencia(Alerta):
    def __init__(self,zona,descripcion):
        self.zona=zona
        self.descripcion=descripcion
    def activar(self):
        super().activar()
        print("--- ⚠️ ALERTA EMERGENCIA ⚠️ ---")
        print(f"Zona: {self.zona}")
        print(f"Descripción: {self.descripcion}")
        print("💀 ¡ACCIÓN INMEDIATA REQUERIDA!")
        