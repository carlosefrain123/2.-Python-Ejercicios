""" Halla la edad del nacimiento de una persona x, incluye exceptions """
try:
    año_actual=int(input("Ingrese el año actual: "))
    año_nacimiento=int(input("Ingrese año de nacimiento: "))
except Exception as e:
    print("Error...")
    print(f'Detalle de e: {e}')
else:
    edad=año_actual-año_nacimiento
    print(f'Año actual: {año_actual}')
    print(f'Año nacimiento: {año_nacimiento}')
    print(f'Edad: {edad}')
finally:
    print("Ejecución terminada")
    