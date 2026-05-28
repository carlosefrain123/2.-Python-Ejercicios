""" Ejercicio 1 — Sistema de combate
Tu equipo necesita un sistema para registrar los combates contra zombies. 
Crea una clase padre Combatiente con atributos nombre y vida, un método atacar que imprima 
"Atacando..." y un método info. Luego crea dos clases hijas Francotirador y Luchador. 
Cada una agrega atributos extra, usa super() y sobreescribe atacar llamando al padre primero. """
from carpetas.Francotirador import Francotirador
from carpetas.Luchador import Luchador

franco  = Francotirador("Efrain", 90, 95)
lucha   = Luchador("Carlos", 100, 80)

franco.info()
# → ⚔️ Efrain | Vida: 90/100

franco.atacar()
# → 💥 Efrain ataca!
# → 🎯 Disparo a distancia con 95% de precisión

lucha.info()
# → ⚔️ Carlos | Vida: 100/100

lucha.atacar()
# → 💥 Carlos ataca!
# → 👊 Golpe cuerpo a cuerpo con 80 de fuerza