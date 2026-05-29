from carpeta.Iventario import Inventario
class InventarioArmas(Inventario):
    def __init__(self, nombre,capacidad_maxima):
        super().__init__(nombre)
        self.capacidad_maxima=capacidad_maxima
    def push(self,item):
        if len(self.items)<self.capacidad_maxima:
            super().push(item)
        else:
            print(f"❌ {self.nombre} lleno [{len(self.items)}/{self.capacidad_maxima}], no entra {item}")
    def estado_arsenal(self):
        print("--- ARSENAL ---")
        print(f"Armas: {self.items}")
        print(f"Capacidad: {len(self.items)}/{self.capacidad_maxima}")
