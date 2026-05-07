""" Ejercicio 2 → Validar datos con múltiples excepciones 
El nombre tiene que ser palabra
print(validar_datos("Ana", 25))    # Ana tiene 25 años
print(validar_datos(123, 25))      # Error: nombre
print(validar_datos("Ana", 200))   # Error: edad
"""
def validar_datos(nombre,edad):
    try:
        if not isinstance(nombre,str):
            raise TypeError
        if edad<0 or edad>120:
            raise ValueError
    except TypeError:
        return "El nombre debe ser una cadena"
    except ValueError:
        return "La edad debe ser menor a 121 años"
    else:
        return f'Me llamo {nombre} y tengo {edad} años'
print(validar_datos("Ana", 25))    # Ana tiene 25 años
print(validar_datos(123, 25))      # Error: nombre
print(validar_datos("Ana", 200))   # Error: edad