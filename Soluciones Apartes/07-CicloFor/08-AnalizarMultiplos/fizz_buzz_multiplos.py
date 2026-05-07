# Mensaje Guía Inicial
print('Vamos A Visualizar "Fizz" Y/O "Buzz" En Los Valores Múltiplos De 3 Y/O 5.')

# Definir E Inicializar Variables Y/O Constantes
step_by_step = 1
initial_number = 0

try:
    # Lectura, Entrada O Ingreso De Datos
    final_number = int(input('Ingresa Un Número Para Definir El Rango Final: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    if (final_number >= 0):
        # Estructura Algorítmica Cíclica for
        for index in range(initial_number, (final_number + 1), step_by_step):
            output = ''

            # Estructura Algorítmica Condicional Simple (Múltiplos De 3)
            if (index % 3 == 0):
                output += 'Fizz'
            
            # Estructura Algorítmica Condicional Simple (Múltiplos De 5)
            if (index % 5 == 0):
                output += 'Buzz'
            
            # Estructura Algorítmica Condicional Compuesto (Mostrar Información Final) 
            if (output):
                print(f'{index} : {output}')
            else:
                print(f'{index} : {index}')
    else:
        print('No Es Posible Desarrollar El Ejercicio.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')