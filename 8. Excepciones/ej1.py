""" Halla la suma de 2 valores, incluy exceptions """
try:
    valor_uno=float(input("Ingrese el valo 1: "))
    valor_dos=float(input("Ingrese el valor 2: "))
except Exception as e:
    print("Error...")
    print(f'"Detalles {e}"')
else:
    suma=valor_uno+valor_dos
    print(f'El valor de a es: {valor_uno}')
    print(f'El valor de b es: {valor_dos}')
    print(f'La suma es: {suma}')
finally:
    print("El bloque del códifo finalizó")