""" Eres desarrollador en Amazon. Tu equipo modela los tipos de envío. 
Crea una clase padre Envio con un método calcular_costo que imprima 
"Calculando costo...". Luego crea dos clases hijas EnvioEstandar 
y EnvioPrime. Cada una sobreescribe calcular_costo con su propio precio.
EnvioEstandar cobra S/15 y EnvioPrime es gratis.
Lo que debes entregar:
- Clase padre: Envio (calcular_costo genérico)
- Clase hija 1: EnvioEstandar (peso, override calcular_costo → S/15)
- Clase hija 2: EnvioPrime (destino, override calcular_costo → gratis)
- 3 objetos: uno de cada clase
- Llamar a calcular_costo() en los 3 """
from carpeta.EnvioEstandar import EnvioEstandar
from carpeta.EnvioPrime import EnvioPrime
envio1=EnvioPrime("Lima")
envio1.calcular_costo()
