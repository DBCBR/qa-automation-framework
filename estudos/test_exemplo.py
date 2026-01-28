import pytest

@pytest.fixture
def numero():
    return 10

def test_numero(numero):
    assert numero == 10
    

@pytest.fixture
def recurso():
    print("Setup")
    yield "ok"
    print("Teardown")

def test_recurso(recurso):
    assert recurso == "ok"