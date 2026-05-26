""" Ejercicio 1 — Uber
Eres desarrollador en Uber. Tu equipo modela los tipos de viaje. 
Crea una clase padre Viaje con atributos origen y destino, un método 
calcular_tarifa que imprima "Calculando..." y un método info que muestre 
origen y destino. Luego crea dos clases hijas UberX y UberBlack. Cada una 
agrega pasajeros y precio_base respectivamente. Ambas usan super(),
sobreescriben calcular_tarifa llamando al padre con super() 
y luego muestran su precio.
Lo que debes entregar:
- Clase padre: Viaje (origen, destino, calcular_tarifa, info)
- Clase hija 1: UberX (hereda + pasajeros + override calcular_tarifa)
- Clase hija 2: UberBlack (hereda + precio_base + override calcular_tarifa)
- super().__init__() y super().calcular_tarifa() en ambas hijas
- 1 objeto de cada hija
- Llamar a info() y calcular_tarifa() """
from carpetas.UberX import UberX
from carpetas.UberBlack import UberBlack
ux=UberX("Chiclayo","Lima",80)
ub=UberBlack("Monsefú","Arequipa",100)

ux.calcular_tarifa()
ub.calcular_tarifa()