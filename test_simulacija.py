import pytest
from sympy import diff
from simulacija import Simulacija

@pytest.fixture
def simulacija():
    return Simulacija(4, 10, 10, 100)

def test_inicijalizacija_cestica(simulacija):
    assert len(simulacija.cestice) == 4 

def test_parovi_cestica(simulacija):
    parovi = simulacija.parovi_cestica() 
    assert len(parovi) == (simulacija.broj_cestica * (simulacija.broj_cestica - 1)) // 2

if __name__ == "__main__":
    pytest.main()