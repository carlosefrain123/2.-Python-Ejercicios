diccionario = {}
while True:
    try:
        zona = input("Ingrese la zona: ")
        if zona.isnumeric():
            print("****No debe ser número, si no cadena de texto.****")
            continue
        cantidad = int(input("Cantidad de zombies eliminados: "))
        if cantidad < 0:
            print("****La cantidad tiene que ser positiva.****")
            continue
    except ValueError:
        print("Error.")
    else:
        if zona in diccionario:
            print("Zona ya registrada")
            diccionario[zona] += (cantidad,)
        else:
            print("Registrando...")
            diccionario[zona] = (cantidad,)
        while True:
            try:
                opcion = int(input("¿Desea Continuar? (1) Sí / (2) No: "))
                if opcion < 1 or opcion > 2:
                    raise ValueError
                break
            except ValueError:
                print("Las opciones tienen que ser 1 y 2")
        if opcion != 1:
            break

# paso 1: calcular totales
totales_por_zona = {}
for zona in diccionario:
    total = 0
    for cantidad in diccionario[zona]:
        total += cantidad
    totales_por_zona[zona] = total

# paso 2: reporte ordenado
print("\n--- Reporte de zonas ---")
for zona in sorted(totales_por_zona.keys()):
    total = totales_por_zona[zona]
    if total >= 100:
        estado = "Zona limpia ✅"
    elif total >= 50:
        estado = "Zona en riesgo ⚠️"
    else:
        estado = "Zona peligrosa ☠️"
    print(f"\n{zona}:")
    print(f"  Total eliminados: {total}")
    print(f"  Estado: {estado}")

# paso 3: mayor y menor
zona_max = max(totales_por_zona, key=totales_por_zona.get)
zona_min = min(totales_por_zona, key=totales_por_zona.get)
print(f"\n{'='*30}")
print(f"🏆 Zona con MAYOR cantidad: {zona_max} ({totales_por_zona[zona_max]} zombies)")
print(f"⚠️  Zona con MENOR cantidad: {zona_min} ({totales_por_zona[zona_min]} zombies)")