# Mensaje Guía Inicial
print('Vamos A Visualizar La Potencia Del Número 2 Como Base.')

try:
    # Lectura, Entrada O Ingreso De Datos
    power_exponent = int(input('Ingrese Un Número Entero Para Usarlo Como Exponente Máximo: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Inicialización De Variables Y/O Constantes
    initial_number = 0
    final_number = (power_exponent + 1)
    step_by_step = 1
    
    # Estructura Algorítmica Cícicla for
    for index in range(initial_number, final_number, step_by_step):
        print(f'2 Elevado A {index} = {2 ** index}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')