""" Inspeccionando el almacén antes de decidir
Tu líder quiere revisar el almacén antes de tomar decisiones.
Solo quiere ver los suministros, no tocarlos.
Lo que debes hacer paso a paso:
1. Crea una pila llamada almacen con estos 5 suministros ya cargados:
   ["Agua potable", "Latas de comida", "Botiquín", "Baterías", "Combustible"]

2. Imprime al inicio:
   "--- INSPECCIÓN DEL ALMACÉN ---"

3. Usa peek ([-1]) para ver el suministro del tope
   Imprime:
   "👁️ Suministro en el tope: [suministro]"

4. Usa peek ([0]) para ver el primer suministro
   Imprime:
   "👁️ Primer suministro: [suministro]"

5. Evalúa con if/elif/else el suministro del tope:
   - Si es "Combustible"   → "⛽ Tenemos combustible, podemos mover vehículos"
   - Si es "Botiquín"      → "💊 Tenemos botiquín, podemos atender heridos"
   - Si es "Baterías"      → "🔋 Tenemos baterías, podemos encender equipos"
   - Cualquier otro        → "📦 Suministro básico disponible"

6. Al final imprime la pila completa para verificar que no cambió:
   "--- VERIFICACIÓN ---"
   "Almacén sin cambios: [pila]"
   "Total suministros: X" """
almacen=["Agua potable", "Latas de comida", "Botiquín", "Baterías", "Combustible"]
print("\n--- INSPECCIÓN DEL ALMACÉN ---")
sTope=almacen[-1]
print(f"👁️ Suministro en el tope: {sTope}")
pSu=almacen[0]
print(f"👁️ Primer suministro: {pSu}")

respuesta="📦 Suministro básico disponible"
for i in almacen:
    if sTope == "Combustible":
        respuesta="⛽ Tenemos combustible, podemos mover vehículos"
        break
    elif sTope=="Botiquín":
        respuesta="💊 Tenemos botiquín, podemos atender heridos"
        break
    elif sTope=="Baterías":
        respuesta="🔋 Tenemos baterías, podemos encender equipos"
        break
print(respuesta)

        