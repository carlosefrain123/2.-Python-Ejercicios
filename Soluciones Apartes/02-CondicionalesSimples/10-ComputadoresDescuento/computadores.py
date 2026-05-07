try:
    # Lectura, Entrada O Ingreso De Datos
    quantity = int(input('Ingrese La Cantidad De Computadoras A Comprar: '))
    unit_price = float(input('Ingrese El Valor De Cada Computadora: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operaciones Aritméticas
    initial_purchase = quantity * unit_price
    iva_tax = initial_purchase * 0.19
    final_purchase = initial_purchase + iva_tax

    # Estructura Condicional Simple
    if (final_purchase >= 1000):
        discount = initial_purchase * 0.10
        total_purchase = final_purchase - discount

        # Mostrar Información Por Consola
        print(f'\nCantidad De Computadoras Compradas => {quantity}')
        print(f'Valor Unitario De Cada Computadora => {unit_price} Dólares.')
        print(f'Valor De La Compra Inicial => {initial_purchase} Dólares.')
        print(f'Valor Del IVA 19% => {iva_tax} Dólares.')
        print(f'Valor De La Compra Final => {final_purchase} Dólares.')
        print(f'Valor Del Descuento 10% => {discount} Dólares.')
        print(f'Valor Total De Facturación => {total_purchase} Dólares.')

    # Estructura Condicional Simple
    if (final_purchase < 1000):
        # Mostrar Información Por Consola
        print(f'\nCantidad De Computadoras Compradas => {quantity}')
        print(f'Valor Unitario De Cada Computadora => {unit_price} Dólares.')
        print(f'Valor De La Compra Inicial => {initial_purchase} Dólares.')
        print(f'Valor Del IVA 19% => {iva_tax} Dólares.')
        print(f'Valor De La Compra Final => {final_purchase} Dólares.')
finally:
    print('El Bloque De Código Finalizo Su Ejecución.\n')