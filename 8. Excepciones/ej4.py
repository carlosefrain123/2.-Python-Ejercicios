""" Ejercicio 1 → Calculadora con excepciones
La operacion lo eligen "+","-","*","/"
rint(calculadora(10, 2, "/"))    # 5.0
print(calculadora(10, 0, "/"))    # Error división
print(calculadora("a", 2, "+"))   # Error valor
""" 
def calculadora(a,b,operador):
    try:
        valor_a=int(a)
        valor_b=int(b)
        if operador=="+":
            return valor_a+valor_b
        elif operador=="-":
            return valor_a-valor_b
        elif operador=="/":
            return valor_a/valor_b
        elif operador=="*":
            return valor_a*valor_b
        else:
            return "Operador no válido"
    except Exception as e:
        print("Error...")
        print(f'Detalles de e: {e}')
    """ except ZeroDivisionError:
        return "No se puede dividir entre 0"
    except ValueError:
        return "Ingrese un número float" """
    
print(calculadora(10, 2, "/"))    # 5.0
print(calculadora(10, 0, "/"))    # Error división
print(calculadora("a", 2, "+"))   # Error valor