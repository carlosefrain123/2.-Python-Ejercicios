class SistemaBunker:
    def __init__(self,nombre):
        self.nombre=nombre
        self.registro=[]
    def push(self,item):
        self.registro.append(item)
        print(f"📋 {self.nombre}: {item} registrado | Total: {len(self.registro)}")
    def pop(self):
        if self.registro:
            quitar=self.registro.pop()
            print(f"✅ {self.nombre}: {quitar} eliminado | Pendientes: {len(self.registro)}")
        else:
            print(f"❌ {self.nombre}: No hay registros")
    def peek(self):
        if self.registro:
            tope=self.registro[-1]
            print(f"🎯 {self.nombre} más urgente: {tope}'")
        else:
            print(f"❌ {self.nombre}: No hay registros")
    def informe(self):
        print("--- INFORME: [nombre] ---")
        print(f"Registro: {self.registro}")
        print(f"Total: {len(self.registro)}")
""" prueba1=SistemaBunker("Bunkerx")
prueba1.push("Arma")
prueba1.push("Cuchillo")
prueba1.push("Botiquin")
prueba1.pop()
prueba1.informe() """

