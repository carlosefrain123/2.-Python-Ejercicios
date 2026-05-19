""" Crea una clase Estudiante con atributos nombre y una lista vacía de notas. 
Agrega métodos para agregar_nota, calcular promedio e imprimir si aprobo (promedio >= 11). """
class Estudiante:
    def __init__(self,nombre):
        self.nombre=nombre
        self.lista_notas=[]
    def agregar_nota(self,nota):
        self.lista_notas.append(nota)
        return f"Nota agrega: {nota}"
    def promedio(self):
        prom=sum(self.lista_notas)/len(self.lista_notas)
        return prom
estudiante1=Estudiante("Efrain")
print(estudiante1.agregar_nota(20))
print(estudiante1.agregar_nota(5))
print(estudiante1.promedio())
