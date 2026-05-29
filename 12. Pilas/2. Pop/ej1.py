""" Distribuyendo suministros al equipo
Tienes el almacén cargado. Tu líder te pide distribuir los suministros 
al equipo de uno en uno empezando por el último que entró.
Lo que debes hacer paso a paso:
1. Crea una pila llamada almacen con estos 5 suministros ya cargados:
   ["Agua potable", "Latas de comida", "Botiquín", "Baterías", "Combustible"]

2. Imprime al inicio:
   "--- DISTRIBUCIÓN DE SUMINISTROS ---"
   "Almacén inicial: [pila]"

3. Distribuye los primeros 3 suministros con pop():
   Después de cada pop() imprime:
   "📤 Distribuido: [suministro] | Quedan en almacén: X"

4. Después de distribuir 3 imprime:
   "--- PAUSA EN LA DISTRIBUCIÓN ---"
   "Suministros distribuidos: 3"
   "Suministros restantes: [pila]"

5. Distribuye los 2 restantes con pop():
   Después de cada pop() imprime:
   "📤 Distribuido: [suministro] | Quedan en almacén: X"

6. Al final imprime:
   "✅ Almacén vacío, todos los suministros distribuidos" """
print("--- DISTRIBUCIÓN DE SUMINISTROS ---")
Almacén_inicial= ['Agua potable', 'Latas de comida', 'Botiquín', 'Baterías', 'Combustible']
quitar1=Almacén_inicial.pop()
print(f"Distribuido: {quitar1} | Quedan en almacén: {len(Almacén_inicial)}")
quitar1=Almacén_inicial.pop()
print(f"Distribuido: {quitar1} | Quedan en almacén: {len(Almacén_inicial)}")
quitar1=Almacén_inicial.pop()
print(f"Distribuido: {quitar1} | Quedan en almacén: {len(Almacén_inicial)}")
quitar1=Almacén_inicial.pop()
print(f"Distribuido: {quitar1} | Quedan en almacén: {len(Almacén_inicial)}")
quitar1=Almacén_inicial.pop()
print(f"Distribuido: {quitar1} | Quedan en almacén: {len(Almacén_inicial)}")
print("✅ Almacén vacío, todos los suministros distribuidos")