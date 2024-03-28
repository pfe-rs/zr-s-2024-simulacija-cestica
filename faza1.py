import math
from sympy import symbols, diff
k = 9 * 10**9
class Cestica():
    def __init__(self, pozicija, brzina, masa, naelektrisanje):
        self.pozicija = pozicija
        self.brzina = brzina
        self.masa = masa
        self.naelektrisanje = naelektrisanje

    @property
    def pozicija(self):
        return self._pozicija

    @pozicija.setter
    def pozicija(self, nova_pozicija):
        self._pozicija = nova_pozicija

    @property
    def brzina(self):
        return self._brzina

    @brzina.setter
    def brzina(self, nova_brzina):
        self._brzina = nova_brzina

    @property
    def masa(self):
        return self._masa

    @masa.setter
    def masa(self, nova_masa):
        self._masa = nova_masa

    @property
    def naelektrisanje(self):
        return self._naelektrisanje

    @naelektrisanje.setter
    def charge(self, novo_naelektrisanje):
        self._naelektrisanje = novo_naelektrisanje

    def __str__(self):
        return f"Particle at pozicija {self.pozicija}, brzina {self.brzina}, masa {self.masa}, naelektrisanje {self.naelektrisanje}"

    def azuriranje_pozicije(self, t):
        self.pozicija = Interakcija.Ojlerov_algoritam(self, t)


class Interakcija:
    def rastojanje(cestica1, cestica2):
        x1, y1 = cestica1.pozicija
        x2, y2 = cestica2.pozicija
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def Lennard_Jonesov_potencijal(cestica1, cestica2, epsilon, sigma):
        r = Interakcija.rastojanje(cestica1, cestica2)
        V = 4 * epsilon[(sigma/r)**12 - (sigma/r)**6]
        return diff(V, r)

    def Kulonov_zakon(cestica1, cestica2):
        r = Interakcija.rastojanje(cestica1, cestica2)
        return k * abs(cestica1.naelektrisanje * cestica2.naelektrisanje) / (r**2)

    def sila(cestica1, cestica2):
        if cestica1.naelektrisanje == 0 and cestica2.naelektrisanje == 0:
            return Interakcija.Lennard_Jonesov_potencijal(cestica1, cestica2)
        else:
            return Interakcija.Kulonov_zakon(cestica1, cestica2)

    def ubrzanje(cestica, sila):
        return sila / cestica.masa
    
    def ukupna_sila():
        pass

    def Ojlerov_algoritam(cestica, t):
        promenjena_pozicija = cestica.pozicija + cestica.brzina * t
        return promenjena_pozicija
        
    def Verletov_algoritam(cestica, sila, t):
        a = Interakcija.ubrzanje(cestica, sila)
        promenjena_pozicija = cestica.pozicija + cestica.brzina * t + (a * t**2)/2
        return promenjena_pozicija

class Simulacija():
    def inicijalizacija_cestica():
        pass
    def parovi_cestica():
        pass