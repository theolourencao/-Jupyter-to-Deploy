import pytest

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200

def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"mensagem": "Olá Mundo!"}

def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_tamanho_lista_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3

def teste_pega_unidade_produto():
    response = client.get("/produtos/1")
    assert response.json() == {
        "id": "1",
        "nome": "Smartphone XYZ",
        "descricao": "Um smartphone de última geração com câmera de alta resolução",
        "preco": "2999.99"
    }
    