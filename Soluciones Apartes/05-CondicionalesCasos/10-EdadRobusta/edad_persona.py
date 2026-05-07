try:
    # Definir E Inicializar Variables
    age = int(input('Ingrese La Edad De Una Persona: '))
except Exception as e:
    print('\nEl Valor Ingresado No Es Válido.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Condicional Compuesta
    if ((age >= 0) and (age <= 120)):
        # Estructura Condicional CASOS
        match (age):
            case (age) if (age <= 17):
                message = 'Eres Menor De Edad.'
            case (age) if (age >= 18):
                message = 'Eres Mayor De Edad.'
            case _:
                message = 'El Valor Ingresado No Es Válido.'

        # Mostrar Información Por Consola
        print(message)
    else:
        print('No Es Posible Trabajar Con Los Valores Ingresados.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')