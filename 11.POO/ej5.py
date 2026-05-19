""" Crea una clase Cajero con atributos nombre y saldo_caja (empieza en 0). 
Agrega métodos cobrar que sume al saldo, dar_vuelto que reste del saldo si hay suficiente, 
y ver_saldo que muestre cuánto hay en caja. """
class Cajero:
    def __init__(self,nombre):
        self.nombre=nombre
        self.saldo_caja=0
    def suma_saldo(self,saldo):
        self.saldo_caja+=saldo
        """ return saldo """
        print(F"Su monto agregado es: {saldo}")
    def resta_saldo(self,saldo):
        if self.saldo_caja>saldo:
            self.saldo_caja-=saldo
            print(f"Su monto descontado es: {saldo}")
        else:
            print("No hay suficiento salfo")
    def ver_saldo(self):
        print(f"El actual monto es: {self.saldo_caja}")
        
cleinte1=Cajero("Efrain|")
cleinte1.suma_saldo(80)
cleinte1.suma_saldo(90)
cleinte1.resta_saldo(20)
cleinte1.ver_saldo()

