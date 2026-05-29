""" Registro de sobrevivientes
Eres el encargado del registro del búnker. Crea una clase padre Sobreviviente con atributos nombre y edad, 
y un método info. Luego crea una clase hija SobrevivienteEspecialista que además tenga especialidad y nivel. 
Usa super() y agrega un método ficha_completa que muestre todos sus datos.
Lo que debes hacer paso a paso:
1. Crea la clase padre Sobreviviente con:
   - Atributos: nombre, edad
   - Método info → imprime:
     "👤 Nombre: [nombre] | Edad: [edad] años"

2. Crea la clase hija SobrevivienteEspecialista con:
   - Atributos heredados: nombre, edad (usando super())
   - Atributos propios: especialidad, nivel
   - Método ficha_completa → imprime:
     "--- FICHA DEL ESPECIALISTA ---"
     "👤 Nombre      : [nombre]"
     "🎂 Edad        : [edad] años"
     "🔧 Especialidad: [especialidad]"
     "⭐ Nivel       : [nivel]/10"

3. Crea estos objetos:
   - Sobreviviente("Luis", 35)
   - SobrevivienteEspecialista("Efrain", 28, "Francotirador", 9)

4. Para cada objeto llama a:
   - Sobreviviente → info()
   - SobrevivienteEspecialista → info() y ficha_completa() """
from carpetas.Sobreviviente import Sobreviviente
from carpetas.SobrevivienteEspecialista import SobrevivienteEspecialista
s=Sobreviviente("Luis", 35)
sE=SobrevivienteEspecialista("Efrain", 28, "Francotirador", 9)
s.info()
sE.info()
sE.ficha_completa()