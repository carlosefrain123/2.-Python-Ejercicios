print('*** Sistema De Navegación De Menús Jerárquicos ***')

# Definir E Inicializar Variables Y/O Constantes
main_choice = 0

# Estructura Algorítmica Cíclica (while Anidado)
while (main_choice != 4):
    print('Menú Principal:')
    print('1. Operaciones De Ventas.')
    print('2. Generación De Reportes.')
    print('3. Configuración Del Sistema.')
    print('4. Salir Del Programa.')
    
    # Capturar Los Valores Ingresados De Forma Incorrecta
    try:
        main_choice = int(input('Seleccione Una Opción Del Menú (1-4): '))
    except Exception:
        print('\nError: Solo Se Permiten Valores Numéricos.\n')
        continue

    # Operatividad Para La Primera Opción Seleccionada
    if (main_choice == 1):
        # Definir E Inicializar Variables Y/O Constantes
        sales_choice = 0
        
        # Estructura Algorítmica Cíclica (while Anidado)
        while (sales_choice != 3):
            print('\nSubmenú De Ventas:')
            print('1. Procesar Nueva Venta.')
            print('2. Manejar Devolución.')
            print('3. Volver al Menú Principal.')
            
            # Capturar Los Valores Ingresados De Forma Incorrecta
            try:
                sales_choice = int(input('Seleccione Una Opción Del Menú De Ventas: '))
            except ValueError:
                print('\nError: Solo Se Permiten Valores Numéricos.')
                continue
    
            # Operatividad Para La Primera Opción Seleccionada (VENTAS)
            if (sales_choice == 1):
                try:
                    amount = float(input('Monto De La Venta: $'))
                    
                    if (amount <= 0):
                        raise ValueError('Ingresar Solo Valores Positivos.')
                    
                    print(f'Venta Procesada: ${amount:,.2f}')
                except ValueError as error:
                    print(f'Error En Venta: {error}')
            elif (sales_choice == 2):
                print('Procesando devolución...')
            elif (sales_choice == 3):
                print('Volviendo al menú principal...\n')
            else:
                print('\nLa Opción Ingresada No Es Válida En El Submenú De Ventas.')
    
    # Operatividad Para La Segunda Opción Seleccionada
    elif (main_choice == 2):
        # Definir E Inicializar Variables Y/O Constantes
        report_choice = 0
        
        # Estructura Algorítmica Cíclica (while Anidado)
        while (report_choice != 4):
            print('\nSubmenú de Reportes: ')
            print('1. Reporte Diario De Ventas.')
            print('2. Análisis De Inventario.')
            print('3. Estadísticas De Clientes.')
            print('4. Volver Al Menú Principal.')
            
            # Capturar Los Valores Ingresados De Forma Incorrecta
            try:
                report_choice = int(input('Seleccione El Tipo De Reporte: '))
            except ValueError:
                print('\nError: Solo Se Permiten Valores Numéricos.')
                continue
            
            if report_choice in {1, 2, 3}:
                print(f'Generando reporte Tipo #{report_choice}...')
            elif report_choice == 4:
                print('Volviendo Al Menú Principal...\n')
            else:
                print('\nLa Opción De Reporte No Es Válida.')
    
    # Operatividad Para La Tercera Opción Seleccionada
    elif (main_choice == 3):
        # Definir E Inicializar Variables Y/O Constantes
        config_choice = 0
        
        # Estructura Algorítmica Cíclica (while Anidado)
        while (config_choice != 3):
            print('\nSubmenú de Configuración: ')
            print('1. Gestión De Usuarios.')
            print('2. Preferencias Del Sistema.')
            print('3. Volver Al Menú Principal.')
            
            # Capturar Los Valores Ingresados De Forma Incorrecta
            try:
                config_choice = int(input('Seleccione La Configuración: '))
            except ValueError:
                print('\nError: Solo Se Permiten Valores Numéricos.')
                continue
    
            if (config_choice == 1):
                print('Gestionando Usuarios...')
            elif (config_choice == 2):
                print('Ajustando Preferencias Del Sistema...')
            elif (config_choice == 3):
                print('Volviendo Al Menú Principal...\n')
            else:
                print('\nLa Opción Ingresada De Configuración No Es Válida.')
    
    elif (main_choice == 4):
        print('\nApagando El Sistema...')
    else:
        print('\nLa Opción Del Menú Principal No Es Válida. Intente Nuevamente.\n')

print('Sistema Apagado Correctamente.')