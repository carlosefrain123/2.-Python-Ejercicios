""" Crea un archivo main.py. Dentro crea una clase padre Cuenta que reciba titular y saldo, 
con un método info que los imprima. Luego crea dos clases hijas CuentaAhorros y CuentaCorriente. 
CuentaAhorros además recibe interes y CuentaCorriente recibe limite_credito. Ambas deben usar super() 
y sobreescribir info llamando primero al padre con super().info() y luego imprimiendo su atributo extra.
Crea un objeto de cada hija y llama a info().
Lo que debes entregar:
- 1 archivo main.py
- Clase padre: Cuenta (titular, saldo, info)
- Clase hija 1: CuentaAhorros (hereda + interes + override de info)
- Clase hija 2: CuentaCorriente (hereda + limite_credito + override de info)
- super().__init__() en ambas hijas
- super().info() dentro del override de ambas hijas
- 1 objeto de cada hija, llamar a info() en cada uno """
from carpetas.Cuentas import Cuentas
from carpetas.CuentaAhorros import CuAh
from carpetas.CuentaCorriente import CuCo
usuario1=Cuentas("Efrain",1800)
usuario2=Cuentas("Brenda",2000)
usuario3=CuAh("Jose",1200,8000)
usuario4=CuCo("Carlos",1200,3)
usuario3.info()
usuario4.info()