try:
    # Lectura, Entrada O Ingreso De Datos
    type = input('Tipo De Vehículo (electrico / hibrido / combustion): ').lower()
    price = float(input('Precio Base Del Vehículo: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}.')
else:
    # Inicialización De Variables Y/O Constantes
    tax = 0
    
    # Estructura Algorítmica Condicional Compuesto (Validando El Tipo De Vehículo Y El Precio)
    if ((type == 'electrico' or type == 'hibrido' or type == 'combustion') and price > 0):
        # Estructura Algorítmica Condicional Anidado (Validando El Tipo De Vehículo)
        if (type == 'electrico' and price <= 30000):
            tax = price * 0.05
        elif (type == 'electrico'):
            tax = price * 0.08
        elif (type == 'hibrido' and price <= 25000):
            tax = price * 0.10
        elif (type == 'hibrido'):
            tax = price * 0.15
        elif (type == 'combustion' and price <= 20000):
            tax = price * 0.20
        elif (type == 'combustion'):
            tax = price * 0.25
        else:
            print('\nTipo De Vehículo No Válido.')

        # Procesos Y Operatividad
        total = price + tax
        
        # Estructura Algorítmica Condicional Simple (Validando El Impuesto)
        if (tax > 0):
            print(f'\nImpuesto Calculado: {tax} Dólares.')
            print(f'Precio Final: {total} Dólares.')
    else:
        print('\nCon Los Datos Ingresados No Se Puede Desarrollar El Planteamiento.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')