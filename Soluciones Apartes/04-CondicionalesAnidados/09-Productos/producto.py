try:
    # Lectura, Entrada O Ingreso De Datos
    product_name = input('Ingrese El Nombre Del Producto: ')
    product_key = input('Ingrese La Clave Del Producto (01 - 02): ')
    original_price = float(input('Ingrese El Precio Del Producto: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Inicialización De Variable De Forma Directa (Bandera)
    is_valid_show_information = True

    # Estructura Condicional Anidado
    if ((product_key == '01') or (product_key == '1')):
        discount = original_price * 0.10
        final_price = original_price - discount
    elif ((product_key == '02') or (product_key == '2')):
        discount = original_price * 0.20
        final_price = original_price - discount
    else:
        is_valid_show_information = False
        print('\nLa Clave Ingresada No Es Válida.')

    if (is_valid_show_information == True):
        # Mostrar Información Por Consola
        print(f'\nNombre Del Producto: {product_name}')
        print(f'Clave Del Producto: {product_key}')
        print(f'Precio Original Del Producto: {original_price} Dólares.')
        print(f'Descuento Del Producto: {discount} Dólares.')
        print(f'Precio Final Del Producto: {final_price} Dólares.')
finally:
    print('El Bloque De Código Termino Su Ejecución.\n')