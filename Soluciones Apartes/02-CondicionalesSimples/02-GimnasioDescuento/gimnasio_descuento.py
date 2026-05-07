try:
    # Lectura, Entrada O Ingreso De Datos
    age = int(input('Ingrese Su edad: '))
    base_price = float(input('Ingrese El Valor De La Mensualidad (Dólares): '))
except Exception as e:
    print('El Valor Ingresado No Es Válido.')
    print(f'Detalle De La Excepción: {e}')
else:
    # Definición E Inicialización De Variables
    discount = 0

    # Estructura Algorítmica Condicional Simple
    if ((age < 18) or (age >= 65)):
        discount = base_price * 0.25
    
    # Procesos Y Operaciones
    total = base_price - discount

    # Mostrar Información Por Consola
    print(f'\nEdad De La Persona: {age} Años.')
    print(f'Pago Mensualidad: {base_price} Dólares.')
    print(f'Descuento Aplicado: {discount} Dólares.')
    print(f'Total A Pagar: {total} Dólares.')
finally:
    print('El Bloque De Código Termino Su Ejecución.')