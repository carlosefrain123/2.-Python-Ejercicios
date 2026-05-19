""" Crea un paquete llamado utilidades con dos módulos: cadenas y numeros. 
En cadenas crea funciones para convertir texto a mayúsculas y contar cuántas vocales tiene.
En numeros crea funciones para saber si un número es par y para calcular su factorial. """
from utilidades import cadenas as cad,numeros as num
print(cad.conta_vocales("Hola mundo"))
print(cad.texto_mayuscula("Hola mundo"))
print(num.num_par(10))
print(num.num_par(5))
print(num.factorial(5))
