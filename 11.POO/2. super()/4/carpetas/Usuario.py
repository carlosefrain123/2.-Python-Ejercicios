class Usuario():
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
    def info(self):
        print(f"Nombre: {self.nombre} | Email: {self.email}")