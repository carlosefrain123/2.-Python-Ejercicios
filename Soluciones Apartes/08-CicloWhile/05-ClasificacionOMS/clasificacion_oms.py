print('*** Clasificación De La OMS, Según El Indice De Masa Corporal (IMC) ***')

try:
    # lectura, Entrada O Ingreso De Datos
    people_count = int(input('Ingrese La Cantidad De Personas A Contabilizar: '))

    # Inicialización De Contadores
    current_person = 0
    underweight_counter = 0
    high_obesity_men_counter = 0
    normal_weight_men_counter = 0
    type3_obesity_women_counter = 0
    
    # Condicional Compuesto Para Válidar Las Personas A Contabilizar
    if (people_count > 0):
        while (current_person < people_count):
            # Lectura, Entrada O Ingreso De Datos
            gender = input(f'Ingrese El Género (m o f) De La Persona #{current_person + 1}: ').lower()
            
            # Condicional Compuesto Para Válidar El Género
            if ((gender == 'm' or gender == 'masculino') or (gender == 'f' or gender == 'femenino')):
                weight = float(input(f'Ingrese El Peso (kg) De La Persona #{current_person + 1}: '))
                height = float(input(f'Ingrese La Estatura (1.67) De La Persona #{current_person + 1}: '))
                
                # Condicional Compuesto Para Válidar El Peso Y La Altura
                if ((weight > 0 and height > 0)):
                    # Procesos Aritméticos Para Válidar El Cálculo Del IMC
                    imc = weight / (height ** 2)
                    
                    # Condicional Anidado Para La Clasificación Del IMC
                    if (imc < 16.0):
                        category = "INFRAPESO => Delgadez Severa.\n"
                    elif (16.0 <= imc < 17.0):
                        category = "INFRAPESO => Delgadez Moderada.\n"
                    elif (17.0 <= imc < 18.5):
                        category = "INFRAPESO => Delgadez Aceptable.\n"
                    elif (18.5 <= imc < 25.0):
                        category = "PESO NORMAL => Peso Normal.\n"
                    elif (25.0 <= imc < 30.0):
                        category = "SOBREPESO => PREOBESO.\n"
                    elif (30.0 <= imc < 35.0):
                        category = "OBESIDAD => Obesidad Tipo I.\n"
                    elif (35.0 <= imc < 40.0):
                        category = "OBESIDAD => Obesidad Tipo II.\n"
                    else:
                        category = "OBESIDAD => Obesidad Tipo III.\n"
                    
                    print(f'Entras En La Categoria De {category}')
                    
                    # Condicional Para Contador General De Infrapeso
                    if (imc < 18.5):
                        underweight_counter += 1
                    
                    # Condicionales Anidados Para La Clasificación Por Género
                    if (gender == 'masculino' or gender == 'm'):
                        if (18.5 <= imc < 25.0):
                            normal_weight_men_counter += 1
                        elif (imc >= 30.0):
                            high_obesity_men_counter += 1
                    elif (gender == 'femenino' or gender == 'f'):
                        if (imc >= 40.0):
                            type3_obesity_women_counter += 1
                    else:
                        print('El Género Ingresado No Es Válido.\n')
                    
                    current_person += 1
                else:
                    print('Los Valores Ingresados No Son Válidos.\n')
            else:
                print('El Género Ingresado No Es Válido.\n')        
    else:
        print('\nNo Es Posible Desarrollar El Ejercicio Algorítmico.')
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Condicional Simple Para Verificar Personas Existentes
    if (current_person > 0):
        # Mostrar Información Por Consola
        print(f'Hombres Con Obesidad: {high_obesity_men_counter}')
        print(f'Hombres Con Peso Normal: {normal_weight_men_counter}')
        print(f'Mujeres Con Obesidad Tipo III: {type3_obesity_women_counter}')
        print(f'Personas Con Infrapeso: {underweight_counter}')
finally:
    print('El Bloque De Código Termino Su Ejecución.')