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