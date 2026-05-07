try:
    # Lectura, Entrada O Ingreso De Datos
    age = int(input('Ingrese La Edad: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Estructura Algorítmica Condicional Compuesto (Validar La Edad)
    if (age >= 0 and age <= 120):
        # Operador Ternario (Validar La Edad)
        price = 5 if (age < 12) else 15
        
        # Mostrar Información Por Consola
        print(f'\nEdad Ingresada: {age}')
        print(f'Precio Final: {price} Dólares.')
    else:
        print('\nLa Edad Ingresada No Es Válida.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')