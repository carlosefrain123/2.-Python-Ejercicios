try:
    # Lectura, Entrada O Ingreso De Datos
    book_type = input('Tipo De Libro (Normal / Reserva): ').lower()
    days_late = int(input('Días De Retraso: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Inicialización De Variables Y/O Constantes
    fine_per_day = 0
    fixed_fine = 0
    
    # Estructura Algorítmica Condicional Simple (Tipo De Libro)
    if (book_type == 'normal'):
        fine_per_day = 0.50
    
    # Estructura Algorítmica Condicional Simple (Tipo De Libro)
    if (book_type == 'reserva'):
        fine_per_day = 1.00
    
    # Estructura Algorítmica Condicional Simple (Retraso Grave)
    if (days_late > 7):
        fixed_fine = 10.00
    
    # Procesos Y Operatividad
    total_per_day = fine_per_day * days_late
    total = total_per_day + fixed_fine
    
    # Estructura Algorítmica Condicional Compuesta (Mostrar Información Por Consola)
    if (fine_per_day == 0 or days_late < 0):
        print('\nEl Tipo De Libro No Es Reconocido O Los Días Ingresados No Son Válidos.')
    else:
        print(f'\nTipo De Libro (Normal / Reserva): {book_type}.')
        print(f'Cantidad De Días De Retraso: {days_late}.')
        print(f'Multa Diaria: {fine_per_day} Dólares.')
        print(f'Multa Adicional: {fixed_fine} Dólares.')
        print(f'Total A Pagar En La Biblioteca: {total} Dólares.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')