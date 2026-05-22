""" Crea una clase Mascota con atributos nombre, especie y energia (empieza en 100). 
Agrega métodos jugar que baje la energía 20 puntos, comer que suba la energía 30 puntos 
y estado que muestre cuánta energía tiene. """
class Mascota:
    def __init__(self,nombre,especie):
        self.nombre=nombre
        self.especie=especie
        self.energia=100
    def jugar(self):
        self.energia-=20
        return f"La energía bajo a {self.energia}"
    def comer(self):
        self.energia+=30
        return f"La energía subio a {self.energia}"
    def estado(self):
        return f"Mascota: {self.nombre} | Especie: {self.especie} | Energía: {self.energia}"
mascota1=Mascota("Boby","Pastor Aleman")
print(mascota1.jugar())
print(mascota1.jugar())
print(mascota1.comer())
print(mascota1.estado())
