""" Sistema de Bono para Empleados
Desarrollar un programa en Python que determine si un empleado 
es elegible para recibir un bono, según sus años de permanencia, 
ventas mensuales y si fue elegido empleado del mes.
Condición                                          Bono
----------------------------------------------------------
Más de 5 años Y ventas > $10,000                   $500.00
Es empleado del mes (independiente de lo demás)    $500.00
Cualquier otro caso                                $0.00
El programa debe:

Solicitar los años de permanencia del empleado en la empresa.
Solicitar las ventas mensuales en dólares.
Preguntar si el empleado fue elegido empleado del mes (Si / No).
Determinar si corresponde un bono de $500.00 o si no aplica bono.
Mostrar un resumen con los años, ventas, estado de empleado del mes y el bono asignado.
Si algún valor ingresado es negativo o no reconocido, mostrar un 
mensaje de inconsistencia en los datos.
Manejar excepciones en caso de valores no válidos.
Mostrar siempre un mensaje de finalización al terminar.

Consideraciones:

Usar la estructura try / except / else / finally.
El bono aplica si se cumple al menos una de las dos condiciones.
Los valores negativos en años o ventas no son válidos.
Las respuestas para empleado del mes solo pueden ser "si" o "no". """
while True:
    try:
        año_perm=int(input("Ingrese los años en permanencia: "))
        if año_perm<0 or año_perm>50:
            print("Los años no deben ser meno a 0 o mayor a 50:")
            continue
        ventas_mensu=float(input("Ingrese las ventas mensuales en dolares: "))
        if ventas_mensu<0:
            print("Las ventas no tienen que ser negativos")
            continue
        empl_mes=int(input("¿Fue elegido como epleado del mes? (1) Sí / (2) No: "))
        if empl_mes<1 or empl_mes>2:
            print("Las ventas tienen que ser 1 o 2: ")
            continue
    except ValueError:
        print("Los valores tienen que ser números, no cadenas de textos:")
    else:
        bono=0
        if (año_perm>5 and ventas_mensu>10000) or empl_mes==1:
            bono=500
        else:
            bono=0
        print(f"Años permanencia: {año_perm} años")
        print(f"Ventas Mensuales: S/. {ventas_mensu}")
        print(f"Bono: S/. {bono}")
        while True:
            try:
                opciones=int(input("¿Desea continuar? (1) Sí / (2) No: "))
                if opciones<1 or opciones>2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones tiene que ser 1 o 2")
        if opciones!=1:
            break
    finally:
        print("Ejecución Terminada.")