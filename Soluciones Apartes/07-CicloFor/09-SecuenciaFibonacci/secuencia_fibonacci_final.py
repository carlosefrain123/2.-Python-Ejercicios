try:
    # Lectura, Entrada O Ingreso De Datos
    number_terms = int(input('Número De Términos A Visualizar: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    if (number_terms >= 0):
        # Procesos Lógicos Y Aritméticos
        initial_number = 0
        next_number = 1

        # Estructura Algorítmica Cíclica for (Mostrar Serie Fibonacci)
        print('Secuencia Fibonacci: ')
        for _ in range(number_terms):
            print(initial_number, end = ' ')
            initial_number, next_number = next_number, initial_number + next_number
    else:
        print('No Es Posible Desarrollar El Ejercicio.')
finally:
    print('\nEl Bloque De Código Termino Su Ejecución.')