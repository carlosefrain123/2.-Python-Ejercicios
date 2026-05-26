""" Crea una clase padre Figura con un método area que imprima "Calculando área..."
. Luego crea dos clases hijas Cuadrado y Triangulo que sobreescriban ese método 
con el cálculo real del área de cada figura. """
from Figuras.Cuadrado import Cuadrado
from Figuras.Triangulo import Triangulo

fig_geo1=Cuadrado(5)
fig_geo2=Triangulo(4,5)

fig_geo1.area()
fig_geo2.area()