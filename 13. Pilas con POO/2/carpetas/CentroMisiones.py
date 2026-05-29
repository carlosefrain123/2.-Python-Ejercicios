from carpetas.SistemaBunker import SistemaBunker
class CentroMisiones(SistemaBunker):
    def __init__(self, nombre,soldados_disponibles):
        super().__init__(nombre)
        self.soldados_disponibles=soldados_disponibles
    def pop(self):
        if self.soldados_disponibles==0:
            print(f"❌ Sin soldados disponibles para la misión")
        elif self.registro:
            super().pop()
            self.soldados_disponibles-=1
            print(f"🪖 Soldado asignado | Disponibles: {self.soldados_disponibles}")
        else:
            print("❌ No hay misiones pendientes")
    def estado_soldados(self):
        print(f"Soladados disponibles: {self.soldados_disponibles}")
    