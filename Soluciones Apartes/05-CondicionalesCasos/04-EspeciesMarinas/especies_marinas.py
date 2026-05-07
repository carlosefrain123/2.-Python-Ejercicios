specie = input('Especie (Tiburon/Pulpo/Ballena): ').lower()

match specie:
    case 'tiburon':
        print('\n🔸Tipo: Cartilaginoso /🔹Hábitat: Oceánico')
    case 'pulpo':
        print('\n🔸Tentáculos: 8 /🔹Camuflaje: Sí')
    case 'ballena':
        print('\n🔸Longitud: 15-30m /🔹Sangre Caliente')
    case _:
        print('\nEspecie No Catalogada.')