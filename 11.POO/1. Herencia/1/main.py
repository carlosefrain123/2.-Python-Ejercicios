""" Crea una clase padre Electrodomestico con atributos marca y precio, 
y métodos encender y apagar. Luego crea dos clases hijas Lavadora y Refrigeradora, 
cada una con un método propio (lavar y enfriar). Crea un objeto de cada una y usa 
todos sus métodos. """
from electrodomesticos.lavadora import Lavadora as l
from electrodomesticos.refrigeradora import Refrigeradora as r

lavadora1=l("Samsung",1000)
refri1=r("LG",5000)
lavadora1.lavar()