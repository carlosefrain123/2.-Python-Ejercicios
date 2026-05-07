print('*** Sistema De Gestión Bibliotecaria ***')  

try:
    # Lectura, Entrada O Ingreso De Datos
    current_loans = 0  
    overdue_books = 0  
    total_books = int(input('Libros Disponibles En La Biblioteca: '))  

    #  Estructura Cíclica While (Mientras Tengamos Libros Prestamos)
    while (total_books > 0):
        action = input('Acción Requerida (Prestar/Devolver/Salir): ').lower()  

        # Condicional Anidado Para Las Acciones De (Prestar/Devolver/Salir)
        if (action == 'prestar'):
            loan_book = int(input('Cantidad De Libros A Prestar: '))  
            
            if (loan_book <= 0 or (loan_book > total_books)):
                print('La Cantidad Ingresada No Es Válida.\n')
                continue

            days = int(input('Días De Préstamo (De 1 A 15): '))
            
            if (days < 1 or days > 15):  
                print('El Plazo Ingresado No Es Válido.\n')  
                continue
            
            # Procesos Y Operaciones
            total_books -= loan_book
            current_loans += loan_book
            
            print(f'Préstamo Registrado. Libros restantes: {total_books}\n')
        elif (action == 'devolver'):  
            returned = int(input('Libros Devueltos: '))  
            delay = int(input('Días De Retraso: '))  

            if (returned <= 0 or (returned > current_loans or delay < 0)):
                print('Antes De Devolver, Verifica Que Tengas Prestamos Activos.')
                print('Los Datos Ingresados No Son Válidos.\n')  
                continue
            
            # Procesos Y Operaciones
            total_books += returned
            current_loans -= returned

            if (delay > 0):
                overdue_books += returned
                print(f'Multa Aplicada: ${delay * 500}')
            
            print('Regreso Registrado Exitosamente.\n')
        elif action == 'salir':
            break
        else:
            print('Acción No Reconocida.\n')  
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Mostrar Información Por Consola
    print('\nReporte Final: ')
    print(f'Libros Disponibles: {total_books}')
    print(f'Préstamos Activos: {current_loans}')
    print(f'Libros Con Multa: {overdue_books}') 
finally:
    print('El Bloque De Código Termino Su Ejecución.')