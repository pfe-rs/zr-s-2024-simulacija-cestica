from interakcija import Interakcija
import math
from sympy import symbols, diff

class Cestica():
    def __init__(self, pozicija, brzina, masa, naelektrisanje):
        self._pozicija = pozicija
        self._brzina = brzina
        self._masa = masa
        self._naelektrisanje = naelektrisanje

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

    def __str__(self):
        return f"Cestica: pozicija {self._pozicija}, brzina {self._brzina}, masa {self._masa}, naelektrisanje {self._naelektrisanje}"

    def azuriranje_pozicije(self, t):
        nova_pozicija = Interakcija.Ojlerov_algoritam(self, t)
        self._pozicija = nova_pozicija

    def azuriranje_brzine(self, sila, t):
        ax, ay = Interakcija.ubrzanje(self, sila)
        self._brzina = (self._brzina[0] + ax * t, self._brzina[1] + ay * t)

