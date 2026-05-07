try:
    # Lectura, Entrada O Ingreso De Datos
    purchase_value = float(input('Ingrese El Valor De La Compra: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Procesos Y Operatividad
    discount = purchase_value * 0.10

    # Operador Ternario (Válidar El Descuento)
    total = purchase_value - discount if (purchase_value > 200) else purchase_value

    # Mostrar Información Por Consola
    print(f'\nTotal A Pagar: {total} Dólares.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')