""" Sistema de armas del búnker
Eres el armero del búnker. Tu líder te pide registrar todos los tipos de 
armas disponibles. Crea una clase padre Arma con atributos nombre y daño, 
y métodos equipar y guardar. Luego crea dos clases hijas ArmaCorta con
un método ataque_rapido y ArmaLarga con un método ataque_precision. 
Crea un objeto de cada hija y llama a todos sus métodos.
Lo que debes hacer paso a paso:
1. Crea la clase padre Arma con:
   - Atributos: nombre, daño
   - Método equipar → imprime: "[nombre] equipada ⚔️"
   - Método guardar → imprime: "[nombre] guardada en el inventario 🎒"

2. Crea la clase hija ArmaCorta que hereda de Arma con:
   - Método ataque_rapido → imprime:
     "[nombre] ataque rápido! Daño: [daño] 💨"

3. Crea la clase hija ArmaLarga que hereda de Arma con:
   - Método ataque_precision → imprime:
     "[nombre] disparo de precisión! Daño: [daño] 🎯"

4. Crea estos objetos:
   - ArmaCorta("Pistola", 30)
   - ArmaLarga("Rifle de francotirador", 90)

5. Para cada objeto llama a todos sus métodos en este orden:
   - equipar()
   - su método propio
   - guardar() """
from carpetas.ArmaCorta import ArmaCorta
from carpetas.ArmaLarga import ArmaLarga
ac1=ArmaCorta("Pistola", 30)
al=ArmaLarga("Rifle de francotirador", 90)

ac1.equipar()
ac1.ataque_rapido()
ac1.guardar()