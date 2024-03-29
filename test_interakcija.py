from cestica import Cestica
from interakcija import Interakcija

cestica1 = Cestica((1, 3), (4, 2), 0.2, 0.03)
cestica2 = Cestica((6, 2), (7, 1), 0.4, 0.04)
r = Interakcija.rastojanje(cestica1, cestica2)
print(r)
F = Interakcija.sila(cestica1, cestica2)
a1 = Interakcija.ubrzanje(cestica1, F)
a2 = Interakcija.ubrzanje(cestica2, F)
print(a1, a2)