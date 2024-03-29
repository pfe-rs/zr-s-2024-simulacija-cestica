from simulacija import Simulacija


simulacija = Simulacija(4, 10, 10, 10) 
cestice = simulacija.inicijalizacija_cestica()
parovi = Simulacija.parovi_cestica(cestice)

for par in parovi:
    print(f"Par čestica: {par[0]} - {par[1]}")