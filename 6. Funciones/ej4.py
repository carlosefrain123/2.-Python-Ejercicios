""" Ejercicio 4 → Reporte completo (usa todas las anteriores) 

Recuerda:
- IMC=peso/(altura)**2
- El peso tiene que ser menor a 120 y mayor que 0
- Si es menor de 50 es "Bajo Peso"
- Si es menor que 90 es "Peso Normal"
- Si mayor a 90 "Sobrepreso"
- Si es invalido, entonces es "Peso invalido"

Ejemplo:
Peso: 70 kg
Altura: 1.75 m
IMC: 22.86
Clasificación: Normal
"""
def validar_peso(peso):
    if peso<0 or peso>120:
        return None
    return peso
def clasificar_peso(peso):
    if validar_peso(peso) is None:
        return "Peso invalido"
    if peso<=50:
        return "Bajo Peso"
    elif peso<=90:
        return "Peso Normal"
    else:
        return "Sobrepeso"

def peso_altura(peso,altura):
    if validar_peso(peso) is None:
        return None
    if altura<1:
        return None
    IMC=round(peso/(altura)**2,2)
    return {
        f'(1) Peso: {peso}  (2) Altura: {altura} (3) IMC: {IMC} (4) Clasificación {clasificar_peso(peso)}'
    }
print(peso_altura(40, 1.75))   # 22.85
