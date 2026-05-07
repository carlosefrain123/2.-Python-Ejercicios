try:
    # Lectura, Entrada O Ingreso De Datos
    quantity = int(input('Ingrese La Cantidad De Articulos: '))
    initial_purchase = float(input('Ingrese El Valor De La Compra: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Inicialización De Variables
    discount = 0
 
    # Estructura Condicional Simple
    if (initial_purchase > 25):
        discount = initial_purchase * 0.20

    # Operaciones Aritméticas
    iva_tax = initial_purchase * 0.16
    final_purchase = (initial_purchase + iva_tax) - discount

    # Mostrar Información Por Consola
    print(f'\nCantidad De Articulos => {quantity}')
    print(f'Valor De La Compra Inicial => {initial_purchase} Dólares.')
    print(f'Valor Del Descuento 20% => {discount} Dólares.')
    print(f'Valor Del Impuesto 16% => {iva_tax} Dólares.')
    print(f'Valor De La Compra Final => {final_purchase} Dólares.')
finally:
    print('El Bloque Termino Su Ejecución.\n')