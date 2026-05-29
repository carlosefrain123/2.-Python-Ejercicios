""" Sistema de alertas
Tu búnker tiene diferentes niveles de alerta. Crea una clase padre Alerta 
con un método activar genérico. Luego crea dos clases hijas AlertaNormal y
AlertaEmergencia. Cada una sobreescribe activar con su propio mensaje.
Lo que debes hacer paso a paso:
1. Crea la clase padre Alerta con:
   - Método activar → imprime:
     "🔔 Alerta activada"

2. Crea la clase hija AlertaNormal con:
   - Atributos: zona, descripcion
   - Override de activar → imprime:
     "--- ALERTA NORMAL ---"
     "📍 Zona       : [zona]"
     "📝 Descripción: [descripcion]"
     "👉 Monitorear la situación"

3. Crea la clase hija AlertaEmergencia con:
   - Atributos: zona, descripcion
   - Override de activar → imprime:
     "--- ⚠️ ALERTA EMERGENCIA ⚠️ ---"
     "📍 Zona       : [zona]"
     "📝 Descripción: [descripcion]"
     "💀 ¡ACCIÓN INMEDIATA REQUERIDA!"

4. Crea estos objetos:
   - Alerta()
   - AlertaNormal("Sector B", "Ruidos sospechosos")
   - AlertaEmergencia("Puerta principal", "ZOMBIES INTENTANDO ENTRAR")

5. Llama a activar() en los 3 objetos en ese orden """
from carpetas.Alerta import Alerta
from carpetas.AlertaEmergencia import AlertaEmergencia
from carpetas.AlertaNormal import AlertaNormal
aN=AlertaNormal("Sector B", "Ruidos sospechosos")
aE=AlertaEmergencia("Puerta principal", "ZOMBIES INTENTANDO ENTRAR")
aN.activar()
aE.activar()