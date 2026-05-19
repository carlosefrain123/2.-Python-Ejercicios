""" Crea un paquete llamado conversor con dos módulos: temperatura y distancia.
En temperatura convierte Celsius a Fahrenheit. 
En distancia convierte kilómetros a millas. Úsalos desde main.py. """
from conversor import distancia as dist, temperatura as temp
print(dist.temp(100))
print(temp.dist(10))