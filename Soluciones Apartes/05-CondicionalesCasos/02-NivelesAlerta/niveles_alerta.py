# Lectura, Entrada O Ingreso De Datos
alert_code = input('Código De Alerta (ROJA/NARANJA/VERDE): ').upper()

# Estructura Algorítmica Condicional CASOS (Validar Alerta De Código)
match alert_code:
    case 'ROJA':
        print('\n✅ Activar Protocolo De Emergencia.')
        print('\n🚨 Aislar Sistemas Críticos.')
    case 'NARANJA':
        print('\n⚠️ Revisar Sistemas Afectados.')
        print('\n🔍 Iniciar Análisis Forense.')
    case 'VERDE':
        print('\n📡 Monitoreo Preventivo.')
    case _:
        print('\n🔴 Código Inválido.')