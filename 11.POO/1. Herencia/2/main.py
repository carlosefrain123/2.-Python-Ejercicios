""" Ejercicio 2
Crea una clase padre Empleado con atributos nombre y sueldo,
y un método trabajar. Luego crea dos clases hijas Programador y Diseñador,
cada una con un método propio (codear y diseñar). 
Crea un objeto de cada una y usa todos sus métodos. """
from profesion.Programador import Programador
from profesion.Diseñador import Diseñador

programador1=Programador("Efrain",3000)
diseñador1=Diseñador("Brenda",5000)

programador1.codear()
diseñador1.diseñar()