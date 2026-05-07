try:
    # Lectura, Entrada O Ingreso De Datos
    number_terms = int(input('Número De Términos A Visualizar: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:    
    # Porcesos Lógicos Y Aritméticos
    a, b = 0, 1

    # Estructura Algorítmica Cíclica for (Mostrar Serie Fibonacci)
    print('Secuencia Fibonacci: ')
    for _ in range(number_terms):
        print(a, end = ' ')
        a, b = b, a + b
finally:
    print('\nEl Bloque De Código Termino Su Ejecución.')