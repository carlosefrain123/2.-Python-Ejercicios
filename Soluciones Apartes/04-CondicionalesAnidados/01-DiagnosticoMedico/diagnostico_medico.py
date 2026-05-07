try:
    # Lectura, Entrada O Ingreso De Datos
    fever = input('¿Tienes Fiebre >38°C? (Si / No): ').lower()
    cough = input('¿Tienes Tos Persistente? (Si / No): ').lower()
    pain = input('¿Tienes Dolor En El Pecho? (Si / No): ').lower()
    dizziness = input('¿Experimenta Mareos? (Si / No): ').lower()
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}.')
else:
    # Estructura Algorítmica Condicional Anidado (Validar Los Inputs Del Usuario)
    if ((pain != 'si' and pain != 'no') or (dizziness != 'si' and dizziness != 'no') or 
        (fever != 'si' and fever != 'no') or (cough != 'si' and cough != 'no')):
        print('\nDebes Ingresar TODOS!! Los Valores Correctamente.')
    else:
        # Estructura Algorítmica Condicional Anidado (Validar El Tipo De Enfermedad)
        if (pain == 'si' and dizziness == 'si'):
            print('\n🚨 ¡Urgencia Cardíaca! Acuda Inmediatamente Al Hospital.')
        elif (fever == 'si' and cough == 'si'):
            print('\n🤒 Posible Gripe. Consulte A Un Médico Y Descanse.')
        else:
            print('\n👨⚕️ Síntomas No Críticos. Programe Una Cita Preventiva.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')