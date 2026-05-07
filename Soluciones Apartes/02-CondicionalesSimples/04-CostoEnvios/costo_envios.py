try:
    # Lectua, Entrada O Ingreso De Datos
    distance_kilometers = float(input('Ingrese La Distancia En Kilómetros: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Inicialización De Variables Y Constantes
    extra_kilometers = 0
    extra_price = 0
    final_price = 0
    base_price = 5.00

    # Estructura Algorítmica Condicional Simple (Validar La Distancia)
    if (distance_kilometers > 10):
        extra_kilometers = distance_kilometers - 10
        extra_price = extra_kilometers * 0.80
    
    final_price = base_price + extra_price 

    if (distance_kilometers >= 0):
        # Mostrar Información Por Consola
        print(f'\nDistancia Inicial: {distance_kilometers} Kilómetros.')
        print(f'Distancia Extra: {extra_kilometers} Kilómetros.')
        print(f'Precio Base Del Envío: {base_price} Dólares.')
        print(f'Precio Extra Del Envío: {extra_price} Dólares.')
        print(f'Precio Final Del Envío: {final_price} Dólares.')
    
    if (distance_kilometers < 0):
        print('\nNo Podemos Trabajar Con Distancias Negativas.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')