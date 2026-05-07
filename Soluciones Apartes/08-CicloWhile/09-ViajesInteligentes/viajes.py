print('*** Planificador De Viajes Personalizado ***')  

try:  
    # lectura, Entrada O Ingreso De Datos
    total_days = int(input('Días Totales De Viaje: '))  
    
    # Condicional Para Validar Los Días
    if (total_days <= 0):
        raise Exception("Los Días Ingresados No Son Válidos.")  

    daily_budget = float(input('Presupuesto Diario (Dólares): '))  
    
    # Condicional Para Validar El Presupuesto
    if (daily_budget <= 0):  
        raise Exception("El Presupuesto Ingresado No Es Válido.")  

    # Definir E Inicializar Variables Y/O Constantes
    current_day = 1  
    total_spent = 0
    activities = []  

    # Estructura Algorítmica Del Ciclo While 
    while (current_day <= total_days):  
        print(f'\nDía {current_day}:')

        activity = input('Actividad Principal: ')
        cost = float(input('Costo Diario (Dolares): '))  

        if (cost < 0 or cost > daily_budget):
            print('El Costo Excede El Presupuesto Ingresado.')  
            continue
        
        # Procesos Y Operaciones
        total_spent += cost
        activities.append(activity)
        current_day += 1
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:  
    print('\nItinerario O Programación Final => ')
    
    # Estructura Algorítmica Del Ciclo for
    for idx, activity in enumerate(activities, 1):  
        print(f'Día {idx}: {activity}')
    
    print(f'Gasto Total: {total_spent} Dólares.')  
finally:  
    print('El Bloque De Código Termino Su Ejecución.')