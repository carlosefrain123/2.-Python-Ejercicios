""" Ejercicio 1 → Registro de gastos con update, del y reporte

Total:
--- Reporte de gastos ---
Agua: total=S/.80.0 promedio=S/.80.0
Luz: total=S/.320.0 promedio=S/.160.0
Total general: S/.400.0 """

diccionario={}
while True:
    try:
        servicios=input("Ingrese el nombre sel servicio:")
        if servicios=="":
            break
        if servicios.isnumeric():
            raise TypeError("El servicio debe ser una cadena, no un número")
        gastos=int(input("Ingrese el gasto:"))
        if gastos<0:
            break
    except Exception as e:
        print("Error...")
        print(f"Detalle: {e}")
    else:
        if servicios in diccionario:
            print("**Servicio ya registrado**")
            diccionario[servicios]+=(gastos,)
        else:
            print("Registrando...")
            diccionario[servicios]=(gastos,)
total_general=0
for servicios in diccionario:
    total=0
    conteo=0
    for gastos in diccionario[servicios]:
        total+=gastos
        conteo+=1
    total_general+=total
    promedio=total/conteo
    print(f"El servicio {servicios} tiene un promedio de {promedio}")
    print(f"El total es {total}")
print(f"El total General es {total_general}")
    
    