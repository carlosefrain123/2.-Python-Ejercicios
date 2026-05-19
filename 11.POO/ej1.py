""" Crea una clase Persona con atributos nombre y edad. 
Agrega un método saludar que imprima una presentación y un método es_mayor_de_edad que devuelva 
True o False según la edad. """

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        return f"Hola mi nombre es {self.nombre} y tengo {self.edad} años"
    def es_mayor_de_edad(self):
        return self.edad>=18
persona1=Persona("Efrain",23)
print(persona1.saludar())
print(persona1.es_mayor_de_edad())
