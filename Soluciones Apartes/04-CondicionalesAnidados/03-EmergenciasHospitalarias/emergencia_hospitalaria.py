try:
    # Lectura, Entrada O Ingreso De Datos
    symptom = input('Síntoma Principal (dolor_torax - hemorragia - fiebre): ').lower()
    pain = int(input('Nivel De Dolor (1-10): '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Definir E Inicializar Variables Y/O Constantes
    priority = ''

    # Estructura Algorítmica Condicional Anidado (Validando Datos Ingresados)
    if ((symptom != 'dolor_torax' or symptom != 'hemorragia' or symptom != 'fiebre') and (pain < 1 or pain > 10)):
        print('\nCon Los Datos Ingresados No Se Puede Desarrollar El Planteamiento.')
    else: 
        # Estructura Algorítmica Condicional Anidado (Validando Síntoma Principal)
        if (symptom == 'dolor_torax' and pain >= 7):
            priority = 'URGENCIA MÁXIMA (Código Rojo).'
        elif (symptom == 'dolor_torax'):
            priority = 'Urgencia Alta (Código Naranja).'
        elif (symptom == 'hemorragia' and pain >= 5):
            priority = 'Urgencia Alta (Código Naranja).'
        elif (symptom == 'hemorragia'):
            priority = 'Urgencia Media (Código Amarillo).'
        elif (symptom == 'fiebre' and pain >= 3):
            priority = 'Urgencia Baja (Código Verde).'
        elif (symptom == 'fiebre'):
            priority = 'Consulta General.'
        else:
            priority = 'Síntoma No Reconocido.'
        
        print(f'\nPrioridad Asignada: {priority}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')