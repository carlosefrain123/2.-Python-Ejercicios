""" Ejercicio 1 → Validar peso """
def validar_peso(peso):
    try:
        if peso<0 or peso>120:
            raise e
        return peso
    except Exception as e:
        print("Error...")
        print(f'Detalle de es: {e}')
print(validar_peso(10))
print(validar_peso(121))
print(validar_peso(-5))

