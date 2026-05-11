""" Ejercicio 2 → Sistema de registro con múltiples excepciones

Resultado:
print(registrar_empleado("Ana", 30, 2500))
print(registrar_empleado(123, 30, 2500))
print(registrar_empleado("Ana", 15, 2500))
print(registrar_empleado("Ana", 30, -100))
{'nombre': 'Ana', 'edad': 30, 'salario': 2500.0, 'salario_anual': 30000.0}
Error de tipo: El nombre debe ser texto
Error de valor: Edad fuera de rango laboral
Error de valor: El salario no puede ser negativo """
def registrar_empleado(nombre,edad,salario):
    try:
        if not isinstance(nombre,str):
            raise TypeError
        """ return nombre """
        edad=int(edad)
        if edad<0:
            raise ValueError
        if salario<0:
            raise ValueError
        return f"{nombre}, tiene un salario anual de {salario*12}"
    except TypeError:
        return "El nombre debe ser texto"
    except ValueError:
        return "El número no tiene que ser negativo"
""" print(registrar_empleado("efra")) """
""" print(registrar_empleado("efra",-1)) """
""" print(registrar_empleado("efra",1,-1000)) """
print(registrar_empleado("Ana", 15, 2500))
