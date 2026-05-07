""" 
Ejercicio 2 → Registro de ventas por vendedor
Guarda todo en un diccionario
Al final muestra los vendedores ordenadas y el promedio de sus ventas
"""
diccionario={}
while True:
    try:
        vendedores=input("Ingrese su nombre: ")
        if vendedores=="":
            break
        ventas=float(input("INgrese sus ventas: "))
        if ventas not in range(-1,10001):
            break
    except Exception as e:
        print("Error...")
        print(f'El detalle del e es: {e}')
    else:
        if vendedores in diccionario:
            print("Vendedor ya registrado")
            diccionario[vendedores]+=(ventas,)
        else:
            print("Guardando...")
            diccionario[vendedores]=(ventas,)
""" print(diccionario) """
for vendedores in sorted(diccionario.keys()):
    total=0
    conteo=0
    for ventas in diccionario[vendedores]:
        total+=ventas
        conteo+=1
    promedio=total/conteo
    print(f'El vendedor {vendedores}, su promedio es: {promedio}')