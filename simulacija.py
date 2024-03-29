import math
from sympy import symbols, diff
import random
from itertools import combinations
from cestica import Cestica
k = 9 * 10**9
class Simulacija():
    def __init__(self, broj_cestica, sirina_okvira, visina_okvira, trajanje):
        self.broj_cestica = broj_cestica
        self.sirina_okvira = sirina_okvira
        self.visina_okvira = visina_okvira
        self.trajanje_animacije = trajanje
        self.cestice = self.inicijalizacija_cestica()

    def inicijalizacija_cestica(self):
        cestice = []
        for _ in range(self.broj_cestica):
            pozicija = [random.uniform(0, self.sirina_okvira), random.uniform(0, self.visina_okvira)]
            brzina = [random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)]
            masa = random.uniform(0.1, 10)
            naelektrisanje = 4
            cestica = Cestica(pozicija, brzina, masa, naelektrisanje)
            cestice.append(cestica)
        return cestice
    
    def parovi_cestica(self): 
        parovi = list(combinations(self.cestice, 2))
        return parovi
    
