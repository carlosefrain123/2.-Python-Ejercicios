""" Crea un paquete llamado geometria con dos módulos: circulo y rectangulo. 
Cada uno debe calcular área y perímetro de su figura. Úsalos desde main.py. """
from geometria import circulo as cir, rectangulo as rect
print(cir.area(5))
print(cir.perimetro(5))
print(rect.area(4,6))
print(rect.perimetro(4,6))