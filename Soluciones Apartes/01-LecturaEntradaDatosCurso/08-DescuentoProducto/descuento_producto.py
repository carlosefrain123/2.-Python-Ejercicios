# Lectura, Entrada O Ingreso De Datos
code = input('Ingrese El Código Del Producto: ')

try:
    original_price = float(input('Ingrese El Precio Del Producto: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Operaciones Aritméticas (Descuento %)
    descount = original_price * 0.25
    final_price = original_price - descount

    # Mostrar Información Por Consola
    print(f'\nCódigo Del Producto: {code}')
    print(f'Precio Original Del Producto: {original_price} Dólares.')
    print(f'Descuento 25%: {descount} Dólares.')
    print(f'Precio Final Del Producto: {final_price} Dólares.')
finally:
    print('El Bloque De Código Finalizo La Ejecución.')