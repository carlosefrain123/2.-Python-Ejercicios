class Canal():
    def __init__(self,nombre,suscriptores):
        self.nombre=nombre
        self.suscriptores=suscriptores
    def publicar(self):
        print(f"Publicando...")
    def info(self):
        print(f"Nombre: {self.nombre} | Suscriptores: {self.suscriptores}")