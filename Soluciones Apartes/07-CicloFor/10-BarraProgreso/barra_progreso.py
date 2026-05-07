import time

try:
    # Lectura, Entrada O Ingreso De Datos
    total_steps = int(input('Duración De La Carga (En Pasos): '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'El Detalle De La Excepción: {e}')
else:
    if (total_steps > 0):
        # Estructura Algorítmica Del Ciclo for (Barra Progreso)
        print('\nIniciando Carga..........🔝')
        for index in range(total_steps + 1):
            percent = (index / total_steps) * 100

            # Cada '█' Representa 2% (Máx 50 Caracteres)
            graphic = '█' * int(percent // 2)

            # Mostrar Información Por Consola    
            print(f"\r[{graphic.ljust(50)}] {percent:.1f}%", end = ' ', flush = True)    

            # Simula Retardo Entre Pasos
            time.sleep(0.3)
        print('\n¡Carga Completada!..........✅')
    else:
        print('No Es Posible Desarrollar El Ejercicio.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')