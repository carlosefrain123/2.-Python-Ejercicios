""" Ejercicio 1: Calculadora de Salario Semanal con Horas Extras
Desarrollar un programa en Python que calcule el salario semanal de un empleado 
según las horas trabajadas, considerando un pago adicional por horas extras.
Horas Trabajadas      Tarifa
----------------------------------------------
Hasta 40 horas        $300.00 por hora
Más de 40 horas       $300.00 hora normal
                      $500.00 hora extra
El programa debe:

Solicitar la cantidad de horas trabajadas en la semana.
Si las horas son 40 o menos, calcular el salario multiplicando las horas por $300.00.
Si las horas superan las 40, calcular:

El salario básico con las primeras 40 horas a $300.00.
Las horas extras restando 40 al total de horas trabajadas.
El salario extra multiplicando las horas extras por $500.00.
El salario total sumando el salario básico más el salario extra.


Mostrar un resumen con las horas trabajadas, salario básico, horas extras, salario extra y salario total.
Si las horas ingresadas son negativas, mostrar un mensaje de valor no válido.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
Las primeras 40 horas siempre se pagan a $300.00 por hora.
A partir de la hora 41 en adelante, cada hora se paga a $500.00.
Las horas negativas no son válidas. """

try:
    cht=int(input("Ingrese la cantidad de horas trabajadas: "))
except ValueError:
    print("Debe ser número y no cadena de texto.")
else:
    if cht>=0:
        if cht<=40:
            pago=cht*300
            horas_extras=0
            pago_extra=0
        else:
            pago=40*300
            horas_extras=cht-40
            pago_extra=horas_extras*500
        pago_total=pago+pago_extra
        print(f"Horas Totales: {cht} horas")
        print(f"Pago primeras 40 horas: S/ {pago}")
        print(f"Horas Extras: {horas_extras} horas extras")
        print(f"Pago horas extra: S/{pago_extra}")
        print(f"Pago Total: S/{pago_total}\n")
    else:
        print("Valor no válido.")
finally:
    print("Fin del programa.")
        
        
        
        