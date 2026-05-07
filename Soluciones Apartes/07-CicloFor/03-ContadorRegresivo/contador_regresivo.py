try:
    # Lectura, Entrada O Ingreso De Datos
    initial_number = int(input('Ingrese Un Valor Numérico Para El Inicio Del Contador: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Inicialización De Variables Y/O Constantes
    final_number = -1
    step_by_step = -1

    # Estructura Algorítmica Cíclica for
    for index in range(initial_number, final_number, step_by_step):
        print(f'⏳ {index}')

    # Mostrar Información Por Consola
    print('¡Tiempo terminado! 🚀')
finally:
    print('El Bloque De Código Termino Su Ejecución.')