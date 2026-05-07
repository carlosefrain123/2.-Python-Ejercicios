try:
    # Lectura, Entrada O Ingreso De Datos (Inicialización)
    code = input('Ingrese El Código Del Articulo: ')
    number_items = int(input('Ingrese La Cantidad De Articulos: '))
    item_unit_price = float(input('Ingrese El Precio Unitario Del Articulo: '))
except Exception as e:
    print('\nLos Valores No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional Compuesto (Valores Negativos)
    if ((number_items >= 0) and (item_unit_price >= 0)):
        # Operaciones Aritméticas
        initial_purchase = number_items * item_unit_price
        iva_tax = initial_purchase * 0.19

        # Estructura Condicional Compuesto
        if (number_items >= 50):
            discount = initial_purchase * 0.10
        else:
            discount = 0

        # Operaciones Aritméticas
        total_purchase = (initial_purchase + iva_tax) - discount

        # Mostrar Información Por Consola
        print(f'\nCódigo Del Articulo: {code}')
        print(f'Cantidad De Articulos: {number_items}')
        print(f'Precio Unitario De Cada Articulo: {item_unit_price} Dólares.')
        print(f'Valor De La Compra Inicial: {initial_purchase} Dólares.')
        print(f'Valor Del IVA 19%: {iva_tax} Dólares.')
        print(f'Valor Del Descuento: {discount} Dólares.')
        print(f'Valor Total De La Compra: {total_purchase} Dólares.')
    else:
        print('\nNo Es Posible Trabajar Con Valores Negativos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')