""" Halla el área de un triángulo
(base * height) / 2
Estructura:
    Try:
    except Exception:
    else:
    finally: """
try:
    base=int(input("Ingrese la base: "))
    altura=int(input("Ingrese la altura: "))
except Exception as e:
    print("Error...")
    print(f'Detalles: {e}')
else:
    area_triangulo=(base*altura)/2
    print(f'El área del triángulo es: {area_triangulo}')
finally:
    print("Ejecución Terminada")