""" Ejercicio 4 → Registro de notas con promedio
 """
diccionario={}
while True:
    try:
        nombre_estudiante=input("Ingrese el nombre del estudiante: ")
        if nombre_estudiante=="":
            break
        notas=int(input("Ingrese las notas de los estudiantes: "))
        if notas not in range(0,21):
            break
    except Exception as e:
        print("Error...")
        print(f'El detalle de es: {e}')
    else:
        if nombre_estudiante in diccionario:
            print("Estudiante ya registrado")
            diccionario[nombre_estudiante]+=(notas,)
        else:
            print("Registrando")
            diccionario[nombre_estudiante]=(notas,)
""" print(diccionario) """
for nombre_estudiante in diccionario:
    conteo=0
    total=0
    for notas in diccionario[nombre_estudiante]:
        total+=notas
        conteo+=1
    promedio=total/conteo
    print(f'El {nombre_estudiante} tiene un promedio de {promedio}')