import pytest
from sympy import diff
from simulacija import Simulacija

@pytest.mark.parametrize("simulacija, broj", [
    (Simulacija(3, 10, 10, 10), 3)
])

def test_inicijalizacija_cestica(simulacija, broj):
    assert len(simulacija.cestice) == broj

@pytest.mark.parametrize("simulacija, broj_parova", [
    (Simulacija(3, 10, 10, 10), 3),
    (Simulacija(5, 10, 10, 10), 10)
])

def test_parovi_cestica(simulacija, broj_parova):
    parovi = simulacija.parovi_cestica() 
    assert len(parovi) == broj_parova