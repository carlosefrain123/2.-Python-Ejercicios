class Bunker:
    def __init__(self,nombre,capacidad):
        self.nombre=nombre
        self.capacidad=capacidad
        self.ocupados=0
    def agregar_sobreviviente(self,nombre_s):
        self.ocupados+=1
        if self.ocupados>self.capacidad:
            print(f"❌ {self.nombre} lleno, no hay espacio")
        else:
            print(f"✅ {nombre_s} ingresó al {self.nombre}")
    def estado(self):
        print(f"🏠 Búnker : {self.nombre}")
        print(f"   Espacio: {self.ocupados}/{self.capacidad}")