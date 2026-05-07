try:
    # Lectura, Entrada O Ingreso De Datos
    temperature = float(input('Temperatura Interna (°C): '))
    oxygen = float(input('Nivel De Oxígeno (%): '))
except Exception as e:
    print('\nLos Valores Ingresados No Son Válidos.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Definir E Inicializar Variables O Constantes
    alert = False

    # Estructura Algorítmica Condicional Compuesto (Validar Temperatura U Oxigeno)
    if (temperature < 15 or temperature > 35 or oxygen < 95):
        alert = True
    else:
        alert = False
    
    # Estructura Algorítmica Condicional Compuesto (Validar El Valor De La Alerta)
    if (alert):
        print('\n🚨 ¡ALERTA CRÍTICA! Condiciones Fuera De Parámetros.')

        # Estructura Algorítmica Condicional Compuesto (Validando Temperatura)
        if (temperature < 15 or temperature > 35):
            print('- Debes Revisar Y Ajustar La Temperatura (Rango Ideal Entre 15°C Y 35°C).')
        
        # Estructura Algorítmica Condicional Compuesto (Validando Oxigeno)
        if (oxygen < 95):
            print('- Debes Revisar Y Ajustar El Sistema De Oxígeno (Porcentaje Ideal Mayor A 95%).') 
    else:
        print('\n✅ Condiciones Estables Para Viajar En La Nave Espacial.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')