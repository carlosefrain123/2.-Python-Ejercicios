""" Halla el producto de 2 valores, incluy exceptions """
try:
    numero1=float(input("Ingrese el número 1: "))
    numero2=float(input("Ingrese el número 2: "))
except Exception as e:
    print("Error...")
    print(f'Detalle del error {e}')
else:
    producto=numero1*numero2
    print(f'El número 1 es: {numero1}')
    print(f'El número 2 es: {numero2}')
    print(f'El producto es: {producto}')
finally:
    print("Ejecución terminada...")