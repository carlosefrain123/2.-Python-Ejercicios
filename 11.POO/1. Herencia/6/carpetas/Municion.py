from carpetas.Recurso import Recurso
class Municion(Recurso):
    def recargar(self,complemento):
        self.cantidad+=complemento
        print(f"Recargando {complemento} balas, total: {self.cantidad}")