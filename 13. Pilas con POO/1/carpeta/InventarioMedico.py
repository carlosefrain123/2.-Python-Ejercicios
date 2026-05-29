from carpeta.Iventario import Inventario
class InventarioMedico(Inventario):
    def __init__(self, nombre,nivel_critico):
        super().__init__(nombre)
        self.nivel_critico=nivel_critico
    def pop(self):
        super().pop()
        if len(self.items)<=self.nivel_critico:
            print(f"⚠️ ALERTA: Suministros médicos críticos")
    def estado_medico(self):
        print("--- MÉDICO ---")
        print(f"Suministros: {self.items}")
        if len(self.items)<=self.nivel_critico:
            print("Estado: ⚠️ CRÍTICO")
        else:
            print("Estado: ✅ NORMAL")
