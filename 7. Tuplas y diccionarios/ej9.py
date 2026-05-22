""" Crea un sistema de registro de notas por materia.
Tu tarea es:
- Pedir materia y nota del estudiante
- Guardar en diccionario con tuplas
- Al final mostrar ordenado:
  * Promedio de cada materia
  * Nota más alta y más baja
  * Estado: promedio >= 11 → "Aprobada ✅"
            promedio <  11 → "Desaprobada ❌" """
diccionario={}
while True:
    try:
        materia=input("Ingrese la meteria del estudiante: ")
        if materia.isnumeric():
            print("La materia debe ser una cadena de texto")
            continue
        notas=int(input("Ingrese la nota del estudiante: "))
        if notas<0 or notas>20:
            print("Las notas deben estar entre 0 y20.")
            continue
    except ValueError:
        print("Error.")
    else:
        if materia in diccionario:
            print("Materia ya registrada.")
            diccionario[materia]+=(notas,)
        else:
            print("Registrando Materia.")
            diccionario[materia]=(notas,)
    for i in diccionario:
        suma=0
        cont=0
        for j in diccionario[i]:
            suma+=j
            cont+=1
        promedio=suma/cont
        print(i,"->",promedio)
    while True:
        try: 
            opcion=int(input("¿Desea Continuar? (1) Sí / (2) No: "))
            if opcion<1 or opcion>2:
                raise ValueError
            break
        except ValueError:
            print("Las opciones tienen que ser 1 o 2")
    if opcion!=1:
        break
    
        