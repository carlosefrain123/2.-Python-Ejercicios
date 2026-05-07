# Lectura, Entrada O Ingreso De Datos
url = input('Ingresa Una URL Completa: ')

# Operador Ternario (Válidar El Protocolo http)
protocolo = ('HTTPS' if url.startswith('https') else 'HTTP' if url.startswith('http') else 'Desconocido')

# Mostrar Información Por Consola
print(f'\nEl Protocolo Utilizado En La URL Ingresada Es: {protocolo}.')