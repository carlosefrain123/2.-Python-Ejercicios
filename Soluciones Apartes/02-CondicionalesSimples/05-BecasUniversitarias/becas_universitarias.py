try:
    # Lectura, Entrada O Ingreso De Datos
    average = float(input('Promedio Académico Del Estudiante (1 Al 5): '))
    projects = int(input('Número De Proyectos De Investigación: '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Inicialización De Variables Y/O Constantes
    academic_scholarship = 'No Aplica'

    # Estructura Algorítmica Condicional Simple (Datos No Válidos) 
    if ((average < 0) or (average > 5) or (projects < 0)):
        print('\nNo Es Posible Trabajar Con Valores Negativos O Fuera De Rango.')
        
    # Estructura Algorítmica Condicional Simple (Validar Si Aplicamos Beca) 
    if ((average >= 4.5) and (average <= 5.0) and (projects >= 1)):
        academic_scholarship = 'Beca Completa'

    # Estructura Algorítmica Condicional Simple (Validar Datos Ingresados) 
    if ((average >= 0) and (average <= 5) and (projects >= 0)):
        print(f'\nPromedio Del Estudiante: {average}')
        print(f'Números De Proyectos: {projects}.')
        print(f'Estado De La Beca: {academic_scholarship}.')
        print('La Beca Aplica Si El Promedio Del Estudiante Es Mayor O Igual A 4.5 Y Más De 1 Proyecto.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')