""" Crea un paquete llamado tienda con dos módulos: 
productos y descuentos. En productos crea funciones 
para calcular el precio total de una compra 
(precio × cantidad). En descuentos crea una función 
que aplique un porcentaje de descuento a un precio. 
Úsalos desde main.py. """
from tienda import descuentos as des,productos as pro
print(pro.precio_total(10,4))
print(des.descuentos(10,40))