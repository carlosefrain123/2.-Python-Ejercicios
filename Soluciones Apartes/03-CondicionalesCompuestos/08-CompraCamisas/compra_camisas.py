try:
    # Lectura, Entrada O Ingreso De Datos
    shirts = int(input('Ingrese La Cantidad De Camisas: '))
    unit_price = float(input('Ingrese El Precio De Cada Camisa: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura De Condicional Compuesto
    if ((shirts >= 0) and (unit_price >= 0)):
        # Operaciones Aritméticas
        initial_purchase = shirts * unit_price

        # Estructura De Condicional Compuesto
        if (shirts >= 3):
            percent = 20
            discount = initial_purchase * 0.20
        else:
            percent = 10
            discount = initial_purchase * 0.10

        # Operaciones Aritméticas
        total_purchase = initial_purchase - discount

        # Mostrar Información Por Consola
        print(f'\nCantidad Camisas: {shirts}.')
        print(f'Precio Unitario: {unit_price} Dólares.')
        print(f'Valor Compra Inicial: {initial_purchase} Dólares.')
        print(f'Valor Descuento {percent}%: {discount} Dólares.')
        print(f'Valor De La Compra Final: {total_purchase} Dólares.')
    else:
        print('\nLos Valores No Son Válidos, No Pueden Ser Negativos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')