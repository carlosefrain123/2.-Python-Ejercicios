from carpetas.Alerta import Alerta
class AlertaEscasez(Alerta):
    def __init__(self,recurso,cantidad):
        self.recurso=recurso
        self.cantidad=cantidad
    def activar(self):
        super().activar()

        print("Alerta Activada, Escasez.")
        print(f"Recurso: {self.recurso}")
        print(f"Cantidad: {self.cantidad}")
    