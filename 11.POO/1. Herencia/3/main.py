from carpetas.Office import Office
from carpetas.Windows import Windows
disp=Windows("Windows 11",199)
disp2=Office("Office 365", 99)

disp.instalar()
disp.desinstalar()

disp2.instalar()
disp.actualizar()
disp2.Office()