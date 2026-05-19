""" Crea una clase Lampara con un atributo encendida (empieza en False). 
Agrega métodos encender, apagar y estado que imprima si está encendida o apagada. """
class Lampara:
    def __init__(self,color):
        self.color=color
        self.encendida=False
    def encender(self):
        self.encendida=True
        return f"Lampara {self.color} esta encendida"
    def apagar(self):
        self.encendida=False
        return f"Lampara {self.color} esta apagada"
    def estado(self):
        if self.encendida:
            return (f"La lámpara {self.color} está ON")
        else:
            return (f"La lámpara {self.color} está Off")
lampara1=Lampara("Azul")
print(lampara1.apagar())
print(lampara1.estado())