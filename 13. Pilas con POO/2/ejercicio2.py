""" Eres el coordinador del búnker. Necesitas un sistema que maneje las misiones pendientes
y las alertas activas. Ambos usan pilas pero se comportan diferente.
Lo que debes hacer paso a paso:
1. Crea la clase padre SistemaBunker con:
   - Atributos: nombre, registros=[]
   - Método push(item) → agrega a la pila e imprime:
     "📋 [nombre]: '[item]' registrado | Total: X"
   - Método pop() → saca de la pila e imprime:
     "✅ [nombre]: '[item]' completado | Pendientes: X"
     Si está vacía imprime:
     "❌ [nombre]: No hay registros"
   - Método peek() → ve el tope e imprime:
     "🎯 [nombre] más urgente: '[item]'"
     Si está vacía imprime:
     "❌ [nombre]: No hay registros"
   - Método informe() → imprime:
     "--- INFORME: [nombre] ---"
     "Registros : [pila]"
     "Total     : X"

2. Crea la clase hija CentroMisiones que hereda de SistemaBunker con:
   - Atributo extra: soldados_disponibles
   - Usa super().__init__()
   - Sobreescribe pop() así:
     Si hay registros Y soldados_disponibles > 0:
       llama a super().pop()
       resta 1 a soldados_disponibles
       imprime: "🪖 Soldado asignado | Disponibles: [soldados_disponibles]"
     Si soldados_disponibles == 0:
       imprime: "❌ Sin soldados disponibles para la misión"
     Si no hay registros:
       imprime: "❌ No hay misiones pendientes"
   - Método propio estado_soldados() → imprime:
     "🪖 Soldados disponibles: [soldados_disponibles]"

3. Crea la clase hija SistemaAlertas que hereda de SistemaBunker con:
   - Atributo extra: nivel_alerta (número del 1 al 10)
   - Usa super().__init__()
   - Sobreescribe push() así:
     llama a super().push() normal
     Después evalúa:
     Si nivel_alerta >= 8 imprime:
     "🚨 NIVEL CRÍTICO [nivel_alerta]/10 ¡BÚNKER EN PELIGRO!"
     Si nivel_alerta >= 5 imprime:
     "⚠️ Nivel moderado [nivel_alerta]/10, mantente alerta"
     Si no imprime:
     "✅ Nivel bajo [nivel_alerta]/10, situación controlada"
   - Sobreescribe informe() así:
     llama a super().informe()
     imprime:
     "Nivel     : [nivel_alerta]/10"
     Si nivel_alerta >= 8 imprime además:
     "⚠️ ¡EVACUAR ZONAS DE RIESGO!"

4. Crea estos objetos:
   - CentroMisiones("Misiones", soldados_disponibles=3)
   - SistemaAlertas("Alertas", nivel_alerta=9)

5. Haz estas operaciones en orden:

   MISIONES:
   - push("Explorar sector norte")
   - push("Conseguir combustible")
   - push("Rescatar a Luis")
   - peek()
   - estado_soldados()
   - informe()
   - pop()    ← asigna soldado
   - pop()    ← asigna soldado
   - pop()    ← asigna soldado
   - pop()    ← sin soldados disponibles
   - estado_soldados()

   ALERTAS:
   - push("Ruidos en puerta trasera")
   - push("ZOMBIES EN SECTOR NORTE")
   - push("HORDA DETECTADA EN PERÍMETRO")
   - peek()
   - informe()
   - pop()
   - informe() """