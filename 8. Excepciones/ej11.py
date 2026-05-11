""" 
Halla el promedio de 3 notas

Estructura:
    Try:
    except Exception:
    else:
    finally:
"""
try:
    nota1=int(input("Ingrese la nota 1: "))
    nota2=int(input("Ingrese la nota 2: "))
    nota3=int(input("Ingrese la nota 3: "))
    if nota1<0 and nota2<0 and nota3<0:
        raise 
except ValueError:
    print("Los valores no tienen que ser negativo")
except Exception as e:
    print("Error...")
    print(f"Detalle: {e}")
else:
    promedio=(nota1+nota2+nota3)/3
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Promedio: {promedio}")
    
    
    