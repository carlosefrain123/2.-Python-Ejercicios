""" - Pide nombre de ciudad y temperatura
- Guarda en diccionario con tuplas
- Al final muestra ordenado:
  * promedio de temperatura
  * temperatura más alta
  * temperatura más baja
  * clasificación:
    promedio >= 25 → "Ciudad calurosa 🥵"
    promedio >= 15 → "Ciudad templada 😊"
    promedio <  15 → "Ciudad fría 🥶" """
diccionario={}
while True:
    try:
        ci=input("Ingrese la ciudad: ")
        if ci.isnumeric():
            print("¡No sebe ser un número la ciudad!")
            continue
        tem=int(input("Ingrese la temperatura: "))
        if tem<0:
            continue
    except ValueError:
        print("Error...")
    else:
        if ci in diccionario:
            print("***Ciudad ya registrada***")
            diccionario[ci]+=(tem,)
        else:
            print("***Registrando***")
            diccionario[ci]=(tem,)
        while True:
            try:
                opcion=int(input("¿Desea conitnuar? (1)Sí / (2)No: "))
                if opcion<1 or opcion>2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones deben 1 o 2")
        if opcion!=1:
            break
for ci in diccionario:
    sum=0
    conteo=0
    for temp in diccionario[ci]:
        sum+=temp
        conteo+=1
    promedio=sum/conteo
    print(f"*La ciudad {ci} tiene un promedio de: {promedio}")
    
            
    