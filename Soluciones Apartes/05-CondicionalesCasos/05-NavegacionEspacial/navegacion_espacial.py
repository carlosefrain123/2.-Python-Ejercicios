space_body = input('Cuerpo Celeste (Luna/Marte/Asteroide): ').lower()

match space_body:
    case 'luna':
        print('\nAltitud Orbital: 100km - Consumo: 1500L')
    case 'marte':
        print('\nVelocidad Entrada: 21,000km/h - Escudo Térmico: Sí')
    case 'asteroide':
        try:
            diameter = float(input('Diámetro Del Cuerpo Espacial (Metros): '))
        except Exception as e:
            print('\nLos Valores Ingresados No Son Válidos.')
            print(f'Detalle De La Excepción: {e}')
        else:
            if (diameter > 100):
                print('\nProtocolo De Evasión.')
            else:
                print('\nMapeo De Superficie.')
        finally:
            print('El Bloque De Código Termino Su Ejecución.')
    case _:
        print('\nDestino No Programado.')