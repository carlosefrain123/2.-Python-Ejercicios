from carpetas.Dispositivo import Dispositivo as disp
class Tablet(disp):
    def __init__(self, marca, bateria,pantalla):
        super().__init__(marca, bateria)
        self.pantalla=pantalla
    def info(self):
        super().info()
        print(f"La pantalla es: {self.pantalla}")
        