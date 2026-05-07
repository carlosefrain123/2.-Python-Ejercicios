# Recomendaciones
print('Ingrese Las Notas En Un Rango Del 1 Al 5 => ')

try:
    # Lectura, Entrada O Ingreso De Datos
    grade_one = float(input('Ingrese La Nota #1: '))
    grade_two = float(input('Ingrese La Nota #2: '))
    grade_three = float(input('Ingrese La Nota #3: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operaciones Aritméticas (PROMEDIO)
    average = (grade_one + grade_two + grade_three) / 3

    # Mostrar Información Por Consola
    print(f'\nNota #1: {grade_one}')
    print(f'Nota #2: {grade_two}')
    print(f'Nota #3: {grade_three}')
    print(f'Promedio Del Estudiante: {average}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')