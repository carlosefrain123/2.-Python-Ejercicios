# Definir E Inicializar Variables Y/O Constantes
step_by_step = 1
final_number = 10
population = 1000
initial_number = 1

# Mensaje Visual Por Consola
print('Año | Población')

# Estructura Algorítmica Cíclica for
for year in range(initial_number, final_number, step_by_step):
    # Crecimiento Poblacional A Una Tasa Del 105% Anual
    population *= 1.05

    # Mostrar Información Por Consola
    print(f'{int(year)} | {int(population)} habitantes.')