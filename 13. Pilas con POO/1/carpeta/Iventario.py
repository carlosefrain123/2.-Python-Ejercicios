class Inventario:
    def __init__(self,nombre):
        self.nombre=nombre
        self.items=[]
    def push(self,item):
        self.items.append(item)
        print(f"📥 {self.nombre}: {item} agregado | Pila: {self.items}")
    def pop(self):
        if self.items:
            sacado=self.items.pop()
            print(f"📤 {self.nombre}: {sacado} usado | Quedan: {self.items}")
        else:
            print(f"❌ {self.nombre} vacío")
    def peek(self):
        if self.items:
            tope=self.items[-1]
            print(f"👁️ {self.nombre} tope: {tope}")
        else:
            print(f"❌ {self.nombre} vacío")