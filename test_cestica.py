import pytest
from cestica import Cestica
from interakcija import Interakcija

@pytest.mark.parametrize("nova_pozicija, vreme", [
    ((1, 1), 1),
    ((2, 2), 2)
])
def test_azuriranje_pozicije(nova_pozicija, vreme):
    cestica = Cestica((0, 0), (1, 1), 1, 0) 
    cestica.azuriranje_pozicije(vreme) 
    assert cestica._pozicija == nova_pozicija

@pytest.mark.parametrize("nova_brzina, sila, vreme", [
    ((6, 2), (5, 1), 1),
    ((7, 9), (3, 4), 2)
])

def test_azuriranje_brzine(nova_brzina, sila, vreme):
    cestica = Cestica((0, 0), (1, 1), 1, 0)
    cestica.azuriranje_brzine(sila, vreme)
    assert cestica._brzina == nova_brzina