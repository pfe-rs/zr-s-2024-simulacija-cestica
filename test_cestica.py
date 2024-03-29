from cestica import Cestica
from interakcija import Interakcija


cestica1 = Cestica((4, 3), (1, 5), 2, 5)
cestica2 = Cestica((1, 4), (7, 3), 3, 2)
sila = Interakcija.sila(cestica1, cestica2)
t = 2 
print(Interakcija.ubrzanje(cestica1, sila))
cestica2.azuriranje_pozicije(t)
cestica1.azuriranje_brzine(sila, t)
print(cestica1)
print(cestica2)