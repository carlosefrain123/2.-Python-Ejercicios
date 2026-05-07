try:
    # Lectura, Entrada O Ingreso De Datos
    grade = int(input('Ingresa Una Nota Entera (Del 1 Al 5): '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Algorítmica Condicional Compuesto (Validar Rango)
    if (grade >= 0 and grade <= 5):
        # Operador Ternario (Válidar Letra Asignada)
        word = ('A' if (grade >= 5) else 'B' if (grade >= 4) else 'C' if (grade >= 3) else 'D' if (grade >= 2) else 'F')
        
        # Mostrar Información Por Consola
        print(f'\nCalificación Numérica: {grade}.')
        print(f'Calificación Literaria: {word}.')
    else:
        print('\nLa Nota Ingresada No Hace Parte Del Rango Válido.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')