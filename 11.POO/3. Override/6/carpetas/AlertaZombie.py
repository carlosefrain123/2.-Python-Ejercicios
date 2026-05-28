from carpetas.Alerta import Alerta
class AlertaZombie(Alerta):
    def __init__(self,zona,cantidad):
        self.zona=zona
        self.cantidad=cantidad
    def activar(self):
        super().activar()
        print("Alerta Zombie cerca: ")
        print(f"Zona: {self.zona}")
        print(f"Cantidad: {self.cantidad}")
    