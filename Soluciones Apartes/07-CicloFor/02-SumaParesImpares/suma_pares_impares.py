# Mensaje Guía Inicial
print('====== Suma De Números Pares E Impares Desde 0 Hasta 51 ======')

# Definir E Inicializar Variables Y/O Constantes
step_by_step = 1
final_number = 51
initial_number = 0
accumulator_odd_numbers = 0
accumulator_even_numbers = 0

# Estructura Algorítmica Cíclica for
for index in range(initial_number, final_number, step_by_step):
    # Estructura Algorítmica Condicional Compuesto (Operador Modulo)
    if (index % 2 == 0):
        accumulator_even_numbers += index
    else:
        accumulator_odd_numbers += index

# Procesos Y Operatividad
sum_even_odd_numbers = accumulator_even_numbers + accumulator_odd_numbers

# Mostrar Información Por Consola
print(f'La Suma De Los Números Pares Es: {accumulator_even_numbers}')
print(f'La Suma De Los Números Impares Es: {accumulator_odd_numbers}')
print(f'La Suma Total De Los Números Pares E Impares Es: {sum_even_odd_numbers}')