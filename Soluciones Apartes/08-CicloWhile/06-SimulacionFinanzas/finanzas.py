print('*** Simulador De Inversiones A Largo Plazo (Dólares) ***')  

try:
    # Lectura, Entrada O Ingreso De Datos
    initial_capital = float(input('Capital Inicial ($): '))  
    monthly_contribution = float(input('Aporte Mensual ($): '))  
    annual_rate = float(input('Tasa Anual (%): ')) / 100  
    target = float(input('Meta Financiera ($): '))  

    # Condicional Para Lanzar Una Excepción
    if (initial_capital <= 0 or monthly_contribution < 0 or annual_rate <= 0 or target <= 0):  
        raise Exception('Todos Los Valores Ingresados Deben Ser Positivos.')

    # Inicialización De Variables Y/O Constantes
    months = 0
    current_amount = initial_capital

    # Estructura Cíclica While (Procesos Aritméticos)
    while (current_amount < target):  
        interest = current_amount * (annual_rate / 12)
        current_amount += interest + monthly_contribution  
        months +=1

        # Mostrar Información Por Consola
        print(f'Mes {months}: ${current_amount}')
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Procesos Y Operaciones Aritméticas
    years = months // 12

    # Mostrar Información Por Consola
    print(f'\n¡Meta Alcanzada En {years} Años Y {months % 12} Meses!')  
finally:  
    print('El Bloque De Código Termino Su Ejecución.')