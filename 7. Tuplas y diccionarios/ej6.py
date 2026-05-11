""" Caso 1 → Registro de horas de estudio por materia
- Pide materia y horas estudiadas
- Guarda en diccionario con tuplas
- Al final muestra ordenado:
  * total de horas por materia
  * promedio de horas
  * materia con más horas """
diccionario={}
while True:
  try:
    materia=input("===Ingrese la materia correspondiente: ")
    if materia=="":
      break
    if materia.isnumeric():
      raise TypeError
    horas_estudiadas=int(input("===Ingrese las horas estudiadas: "))
    if horas_estudiadas not in range(0,25):
      break
  except TypeError:
    print(("La materia es una cadena no un número"))
  except Exception as e:
    print("Error...")
    print(f"El detalle es: {e}")
  else:
    if materia in diccionario:
      print("Materia ya registrada")
      diccionario[materia]+=(horas_estudiadas,)
    else:
      print("Registrando...")
      diccionario[materia]=(horas_estudiadas,)
max_promedio=0
materia_maxima=""
for materia in sorted(diccionario.keys()):
  total=0
  conteo=0
  for horas_estudiadas in diccionario[materia]:
    total+=horas_estudiadas
    conteo+=1
  promedio=total/conteo
  """ print(f"La materia {materia}, tiene un total de {total}") """
  if total>max_promedio:
    max_promedio=total
    materia_maxima=materia
  print(f"La materia {materia}, tiene un promedio de {promedio}") #Check
print(f"La materia con más horas es {materia_maxima} con {max_promedio} horas")