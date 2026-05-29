""" Cargando suministros al búnker
Tu equipo acaba de regresar de una misión y encontró varios suministros. 
Debes registrarlos en la pila del almacén uno por uno.
Lo que debes hacer paso a paso:
1. Crea una pila vacía llamada almacen

2. Agrega estos 5 suministros en este orden:
   - "Agua potable"
   - "Latas de comida"
   - "Botiquín"
   - "Baterías"
   - "Combustible"

3. Después de agregar cada suministro imprime:
   "📥 Ingresó: [suministro] | Almacén: [pila]"

4. Al final imprime:
   "--- RESUMEN DEL ALMACÉN ---"
   "Total suministros: X"
   "Último en entrar: [tope]"
   "Primero en entrar: [primero]" """
pila=[]
pila.append("Agua Potable")
pila.append("Latas de comida")
pila.append("Botiquín")
pila.append("Combustible")
print(pila)
print("\n--- RESUMEN DEL ALMACÉN ---")
print(f"Total de suministros: {len(pila)}")
print(f"Ultimo a entrar: {pila[-1]}")
print(f"Primero a entrar: {pila[0]}")

