""" Ejercicio 1 — Sistema de inventario del búnker
Eres el encargado del inventario del búnker. Tu líder te pide crear un sistema que maneje el 
inventario de armas y el inventario médico por separado. Cada inventario tiene su propia pila 
y su propio comportamiento.
Lo que debes hacer paso a paso:
1. Crea la clase padre Inventario con:
   - Atributos: nombre, items=[]
   - Método push(item) → agrega a la pila e imprime:
     "📥 [nombre]: [item] agregado | Pila: [pila]"
   - Método pop() → saca de la pila e imprime:
     "📤 [nombre]: [item] usado | Quedan: [pila]"
     Si está vacía imprime:
     "❌ [nombre] vacío"
   - Método peek() → ve el tope e imprime:
     "👁️ [nombre] tope: [item]"
     Si está vacía imprime:
     "❌ [nombre] vacío"

2. Crea la clase hija InventarioArmas que hereda de Inventario con:
   - Atributo extra: capacidad_maxima
   - Usa super().__init__()
   - Sobreescribe push() así:
     Si la pila tiene menos items que capacidad_maxima:
       llama a super().push() y agrega normal
     Si no:
       imprime: "❌ Arsenal lleno [X/capacidad_maxima], no entra [item]"
   - Método propio estado_arsenal() → imprime:
     "--- ARSENAL ---"
     "Armas    : [pila]"
     "Capacidad: [len(items)]/[capacidad_maxima]"

3. Crea la clase hija InventarioMedico que hereda de Inventario con:
   - Atributo extra: nivel_critico (si quedan igual o menos items que esto, es crítico)
   - Usa super().__init__()
   - Sobreescribe pop() así:
     llama a super().pop() normal
     Después evalúa: si quedan igual o menos items que nivel_critico imprime:
     "⚠️ ALERTA: Suministros médicos críticos"
   - Método propio estado_medico() → imprime:
     "--- MÉDICO ---"
     "Suministros: [pila]"
     Si len(items) <= nivel_critico imprime:
     "Estado     : ⚠️ CRÍTICO"
     Si no imprime:
     "Estado     : ✅ NORMAL"

4. Crea estos objetos:
   - InventarioArmas("Arsenal", capacidad_maxima=4)
   - InventarioMedico("Enfermería", nivel_critico=2)

5. Haz estas operaciones en orden:

   ARSENAL:
   - push("Pistola")
   - push("Escopeta")
   - push("Rifle")
   - push("Machete")
   - push("Granada")    ← debe rechazarse, arsenal lleno
   - peek()
   - estado_arsenal()
   - pop()
   - estado_arsenal()

   ENFERMERÍA:
   - push("Vendas")
   - push("Morfina")
   - push("Botiquín")
   - push("Adrenalina")
   - peek()
   - estado_medico()
   - pop()
   - pop()
   - pop()              ← aquí debe salir alerta crítica
   - estado_medico() """