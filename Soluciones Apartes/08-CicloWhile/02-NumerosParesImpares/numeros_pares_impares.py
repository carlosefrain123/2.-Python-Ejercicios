print('*** Sistema De Procesamiento De Números Pares E Impares ***')

try:
    # Lectura De Datos Y Validación Inicial
    integer_quantity = int(input('Ingrese La Cantidad De Números Enteros Que Vas A Contabilizar: '))
    
    # Inicialización De Variables Y/O Constantes
    index = 0
    even_counter = 0
    odd_counter = 0
    even_accumulator = 0
    odd_accumulator = 0
    odd_average = 0.0

    # Estructura Cíclica While (Lógica Números)
    while (index < integer_quantity):
        # Lectura, Entrada O Ingreso De Datos
        user_number = int(input(f'Ingrese El Valor Numérico #{index + 1}: '))
        
        # Validación Y Clasificación De Números (Pares E Impares)
        if (user_number % 2 == 0):
            even_counter += 1
            even_accumulator += user_number
        else:
            odd_counter += 1
            odd_accumulator += user_number
        
        index += 1
except Exception as error:
    print('\nError: Los Valores Ingresados No Son Válidos.')
    print(f'Detalle Del Error: {error}')
else:
    # Cálculo Del Promedio De Números Impares
    if (odd_counter != 0):
        odd_average = odd_accumulator / odd_counter

    # Mostrar Información Por Consola
    print('\nLa Cantidad De Números Pares Son:', even_counter)
    print('La Suma De Los Números Pares Es:', even_accumulator)
    print('El Promedio De Los Números Impares Es:', odd_average)
finally:
    print('El Bloque De Código Termino Su Ejecución.')