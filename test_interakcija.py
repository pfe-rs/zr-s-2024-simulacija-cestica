import math
from sympy import symbols, diff
from interakcija import Interakcija 
from cestica import Cestica
import pytest
k = 9 * 10**9

def test_rastojanje():
    cestica1 = Cestica((1, 2), (3, 4), 5, 6)
    cestica2 = Cestica((4, 5), (6, 7), 8, 9)
    assert Interakcija.rastojanje(cestica1, cestica2) == math.sqrt((1 - 4)**2 + (2 - 5)**2)

def test_Kulonov_zakon():
    cestica1 = Cestica((1, 2), (3, 4), 5, 6)
    cestica2 = Cestica((4, 5), (6, 7), 8, 9)
    assert Interakcija.Kulonov_zakon(cestica1, cestica2) == (k * abs(cestica1._naelektrisanje * cestica2._naelektrisanje) / (Interakcija.rastojanje(cestica1, cestica2)**3) * abs(4 - 1), k * abs(cestica1._naelektrisanje * cestica2._naelektrisanje) / (Interakcija.rastojanje(cestica1, cestica2)**3) * abs(5 - 2))

def test_ubrzanje():
    cestica = Cestica((1, 2), (3, 4), 5, 6)
    sila = (1, 2)
    assert Interakcija.ubrzanje(cestica, sila) == (1 / 5, 2 / 5)

def test_ukupna_sila():
    sile = [(1, 2), (3, 4), (5, 6)]
    assert Interakcija.ukupna_sila(sile) == (1 + 3 + 5, 2 + 4 + 6)

def test_Ojlerov_algoritam():
    cestica = Cestica((1, 2), (3, 4), 5, 6)
    t = 2
    assert Interakcija.Ojlerov_algoritam(cestica, t) == (1 + 3 * t, 2 + 4 * t)

if __name__ == "__main__":
    pytest.main()