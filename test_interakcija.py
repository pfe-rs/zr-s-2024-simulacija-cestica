import math
from sympy import symbols, diff
from interakcija import Interakcija 
from cestica import Cestica
import pytest
k = 9 * 10**9

@pytest.mark.parametrize("novo_rastojanje, cestica1, cestica2", [
    (math.sqrt(18), Cestica((1, 2), (3, 4), 5, 6), Cestica((4, 5), (6, 7), 8, 9)),
    (math.sqrt(5), Cestica((5, 4), (6, 7), 8, 9), Cestica((4, 6), (6, 7), 8, 9), )
])
def test_rastojanje(novo_rastojanje, cestica1, cestica2):
    assert Interakcija.rastojanje(cestica1, cestica2) == novo_rastojanje

@pytest.mark.parametrize("trazena_sila, cestica1, cestica2", [
    ((round(27 * (10**9) / math.sqrt(2)), round(27 * (10**9) / math.sqrt(2))), Cestica((1, 2), (3, 4), 5, 6), Cestica((4, 5), (6, 7), 8, 9))
])
def test_Kulonov_zakon(trazena_sila, cestica1, cestica2):
    x, y = Interakcija.Kulonov_zakon(cestica1, cestica2)
    x1 = round(x)
    y1 = round(y)
    assert (x1, y1) == trazena_sila

@pytest.mark.parametrize("trazeno_ubrzanje, cestica, sila", [
    ((1 / 5, 2 / 5), Cestica((1, 2), (3, 4), 5, 6), (1, 2))
])
def test_ubrzanje(trazeno_ubrzanje, cestica, sila):
    assert Interakcija.ubrzanje(cestica, sila) == trazeno_ubrzanje

@pytest.mark.parametrize("sile, trazena_sila", [
    ([(1, 2), (4, 5), (7, 1)], (12, 8))
])

def test_ukupna_sila(sile, trazena_sila):
    assert Interakcija.ukupna_sila(sile) == trazena_sila

@pytest.mark.parametrize("trazena_pozicija, cestica, vreme", [
    ((4, 6), Cestica((1, 2), (3, 4), 3, 4), 1), 
])

def test_Ojlerov_algoritam(trazena_pozicija, cestica, vreme):
    assert Interakcija.Ojlerov_algoritam(cestica, vreme) == trazena_pozicija