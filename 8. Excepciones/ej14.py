""" A un empleado le retienen el 12% de su salario básico. Calcular el salario Neto,
sabiendo que le entregan un bono del 2.3% del salario básico. Se debe leer el salario
básico del empleado.

Estructura:
    Try:
    except Exception:
    else:
    finally: """
try:
    nombre=input("Introduce tu nombre: ")
    if nombre.isnumeric():
        raise TypeError("El nombre tiene que ser una cadena")
    salario_basico=float(input("Introduzca su salario: "))
    if salario_basico<0:
        raise ValueError("El salario o tiene que ser negativo")
except Exception as e:
    print("Error...")
    print(f"Detalle: {e}")
else:
    descuento=salario_basico*0.12
    bono=salario_basico*0.023
    total=(salario_basico+bono)-descuento
    print(f"Salario base: {salario_basico}")
    print(f"Bono: {bono}")
    print(f"Descuento: {descuento}")
    print(f"Total: {total}")
finally:
    print("Ejecución terminado")