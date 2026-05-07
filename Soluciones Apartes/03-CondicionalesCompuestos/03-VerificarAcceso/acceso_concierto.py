try:
    age = int(input('Ingrese Su Edad: '))
    vip_entry = input('¿Tiene Entrada VIP? (Si / No): ').lower()
    parental_permission = input('¿Tiene Permiso Parental? (Si / No): ').lower()
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Definir E Inicializar Variables Y/O Constantes
    access = False

    # Estructuras Algorítmicas Condicional Compuesto (Validar Edad Y/O Entrada Y/O Permiso)
    if ((age >= 18 and vip_entry == 'si') or (age < 18 and parental_permission == 'si')):
        access = True
    else:
        access = False

    # Mostrar Información Por Consola (Validando El Acceso)
    if ((access == True) and (age >= 0) and (age <= 100)):
        print('\n✅ Acceso Permitido. ¡Disfrute El Concierto!')
    else:
        if ((access == False) and (age >= 0) and (age <= 100)):
            print('\n❌ Acceso Denegado. No Cumple Los Requisitos.')
        else:
            print('\nTenemos Inconsistencia En La Entrada De Datos.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')