""" Ejercicio 2 → Clasificar peso (usa función anterior) 
- Si es menor de 50 es "Bajo Peso"
- Si es menor que 90 es "Peso Normal"
- Si mayor a 90 "Sobrepreso"
- Si es invalido, entonces es "Peso invalido"

print(clasificar_peso(45))   # Bajo peso
print(clasificar_peso(70))   # Peso normal
print(clasificar_peso(100))  # Sobrepeso
print(clasificar_peso(400))  # Peso inválido
"""
def validar_peso(peso):
    if peso<0 or peso>120:
        return None
    return peso
   
def clasificar_peso(peso):
    if validar_peso(peso) is None:
        return "Peso inválido"
    if peso<=45:
        return "Bajo Peso"
    elif peso<=70:
        return "Peso Normal"
    else:
        return "Sobrepreso"
print(clasificar_peso(45))   # Bajo peso
print(clasificar_peso(70))   # Peso normal
print(clasificar_peso(100))  # Sobrepeso
print(clasificar_peso(400))  # Peso inválido