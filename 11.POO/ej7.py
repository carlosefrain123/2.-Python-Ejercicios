""" Crea una clase Celular con atributos marca, bateria (empieza en 100) y
encendido (empieza en True). Agrega métodos usar_app que baje la batería 15%,
cargar que suba la batería 20%, y apagar que cambie el estado y muestre un mensaje. """
class Celular:
    def __init__(self,marca):
        self.marca=marca
        self.bateria=100
        self.encedido=True
    def usar_app(self):
        if self.bateria>15:
            self.bateria-=15
            return f"Batería al {self.bateria}%"
        else:
            return "Se apagó bateria"
    def cargar(self):
        self.bateria+=15
        if self.bateria>=100:
            self.bateria=100
        return f"Batería al {self.bateria}%"
    def apagar(self):
        self.encedido=False
        if self.encedido==False:
            return f"Se apagó la batería."
celular1=Celular("Samsung")
print(celular1.usar_app())
print(celular1.usar_app())
print(celular1.usar_app())
print(celular1.usar_app())
print(celular1.usar_app())
print(celular1.usar_app())
print(celular1.usar_app())
print(celular1.usar_app())



