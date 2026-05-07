# Lectura, Entrada O Ingreso De Datos
password = input('Ingresa Una Contraseña Mayor O Igual A 8 Caracteres: ')

# Operador Ternario (Validar La Password)
valid = 'Válida' if (len(password) >= 8) else 'Inválida (Mínimo 8 Caracteres)'
    
# Mostrar Información Por Consola
print(f'\nLa Contraseña Ingresada Es: {valid}')