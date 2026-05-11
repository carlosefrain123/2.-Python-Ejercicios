""" Ejercicio 1 → Calculadora con historial
print(calcular(10, 2, "/"))    # 5.0
print(calcular(10, 0, "/"))    # Error
print(calcular("a", 2, "+"))   # Error
print(calcular(5, 3, "+"))     # 8.0

5.0
Error: no puedes dividir entre cero
Error: operación o valores inválidos
8.0

--- Historial ---
10.0 / 2.0 = 5.0
5.0 + 3.0 = 8.0 """

def calcular(numa,numb,operador):
    try:
        numa=int(numa)
        numb=int(numb)
        if numa<0:
            return None
        if numb<0:
            return None
        if operador=="/":
            return numa/numb
        elif operador=="+":
            return numa+numb
        elif operador=="-":
            return numa-numb
        elif operador=="*":
            return numa*numb
        else:
            return "Operador no diponible"
    except ValueError:
        return f"Los números deben ser enteros..."
    except ZeroDivisionError:
        return "No se puede dividir entre 0"
        
print(calcular(-1, 4, "/"))    # 5.0
print(calcular("a", 2, "+"))   # Error
print(calcular(10, 0, "/"))    # Error
