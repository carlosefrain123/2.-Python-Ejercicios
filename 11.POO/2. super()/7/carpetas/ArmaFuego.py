from carpetas.Arma import Arma
class ArmaFuego(Arma):
    def __init__(self, nombre, daño,balas,alcance):
        super().__init__(nombre, daño)
        self.balas=balas
        self.alcance=alcance
    def disparar(self):
        self.balas-=1
        if self.balas<0:
            print("No hay balas")
        else:
            print(f"Hay {self.balas}")