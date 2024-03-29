import pytest
from cestica import Cestica

def test_azuriranje_pozicije():
    cestica = Cestica((0, 0), (1, 1), 1, 0) 
    cestica.azuriranje_pozicije(1) 
    nova_pozicija = cestica._pozicija
    assert nova_pozicija == (1, 1) 

def test_azuriranje_brzine():
    cestica = Cestica((0, 0), (1, 1), 1, 0) 
    cestica.azuriranje_brzine((2, 2), 1) 
    nova_brzina = cestica._brzina
    assert nova_brzina == (3, 3) 

if __name__ == "__main__":
    pytest.main()