""" Ejercicio 3 → Calcular IMC (usa funciones anteriores) 
    IMC=peso/(altura)**2
Recuerda:
- El peso tiene que ser menor a 120 y mayor que 0
- Si es menor de 50 es "Bajo Peso"
- Si es menor que 90 es "Peso Normal"
- Si mayor a 90 "Sobrepreso"
- Si es invalido, entonces es "Peso invalido"

print(calcular_imc(70, 1.75))   # 22.85
print(calcular_imc(70, 0))      # None
print(calcular_imc(400, 1.75))  # None
"""
def validar_altura(peso):
    if peso<0 or peso>120:
        return None
    return peso
def calcular_imc(peso,altura):
    if altura<1:
        return None
    if validar_altura(peso) is None:
        return None
    IMC=round(peso/(altura)**2,2)
    return IMC
print(calcular_imc(70, 1.75))   # 22.85
print(calcular_imc(70, 0))      # None
print(calcular_imc(400, 1.75))  # None

