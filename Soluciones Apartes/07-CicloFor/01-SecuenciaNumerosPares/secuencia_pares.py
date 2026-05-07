# Mensaje Guía Inicial
print('Vamos A Visualizar La Secuencia De Números Pares Que Existe Entre El Cero Y Un Número Ingresado.')

try:
    # Lectura, Entrada O Ingreso De Datos
    limit = int(input('Ingrese Un Valor Numérico: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Inicialización De Variables Y/O Constantes
    initial_number = 0
    final_number = (limit + 1)
    step_by_step = 2

    # Estructura Algorítmica Cíclica for
    for index in range(initial_number, final_number, step_by_step):
        print(f'🔢 {index}', end = ' ')
finally:
    print('\nEl Bloque De Código Termino Su Ejecución.')