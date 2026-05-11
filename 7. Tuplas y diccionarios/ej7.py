""" Caso 2 → Control de asistencia
- Pide nombre del alumno y si asistió (1=presente, 0=ausente)
- Guarda en diccionario con tuplas
- Al final muestra ordenado:
  * total de días presentes
  * total de días ausentes
  * porcentaje de asistencia """
diccionario={}
while True:
  try:
    nombre=input("***Ingrese el nombre del estudiante: ")
    if nombre=="":
      break
    if nombre.isnumeric():
      raise TypeError
    asistencia=int(input("**Ingese si asistió (1=presente, 0=ausente): "))
    if asistencia not in range(-1,2):
      break
  except TypeError:
    print("El nombre es una cadena")
  except ValueError:
    print("La asistencia tiene que ser un número (1 o 0)")
  else:
    if nombre in diccionario:
      print("**Nombre ya registrado**")
      diccionario[nombre]+=(asistencia,)
    else:
      print("**Registrando...")
      diccionario[nombre]=(asistencia,)

for nombre in diccionario:  
  conteo_presente=0
  conteo_ausente=0
  conteo_dias=0
  for asistencia in diccionario[nombre]:
    conteo_dias+=1
    if asistencia==1:
      conteo_presente+=1
    else:
      conteo_ausente+=1
    procentaje_de_asistencias=round((conteo_presente/conteo_dias)*100,1)
  print(f"El alumno {nombre} tiene {conteo_dias} días")
  print(f"El alumno {nombre} tiene {conteo_presente} asistencias y {conteo_ausente} ausencias")
  print(f"El porcentaje del alumno {nombre} es {procentaje_de_asistencias}%")
   
  