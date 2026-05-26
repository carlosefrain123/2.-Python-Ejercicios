class Contenido():
    def __init__(self,titulo,año):
        self.titulo=titulo
        self.año=año
    def reproducir(self):
        print(f"La película {self.titulo}, está reproduciendo.")