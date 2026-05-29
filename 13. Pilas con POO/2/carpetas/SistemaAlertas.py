from carpetas.SistemaBunker import SistemaBunker
class SistemaAlertas (SistemaBunker):
    def __init__(self, nombre,nivel_alerta):
        super().__init__(nombre)
        self.nivel_alerta=nivel_alerta
    def push(self,item):
        super().push(item)
        if self.nivel_alerta>=8:
            print("🚨 NIVEL CRÍTICO [nivel_alerta]/10 ¡BÚNKER EN PELIGRO!")
        elif self.nivel_alerta>=5:
            print("⚠️ Nivel moderado [nivel_alerta]/10, mantente alerta")
        else:
            print("✅ Nivel bajo [nivel_alerta]/10, situación controlada")
    def informe(self):
        super().informe()
        print(f"Nivel: {self.nivel_alerta}/10")
        if self.nivel_alerta>=8:
            print("⚠️ ¡EVACUAR ZONAS DE RIESGO!")