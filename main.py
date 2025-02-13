from fastapi import FastAPI
from typing import List, Dict


produtos: List[Dict[str, any]] = [
    {
        "id": "1",
        "nome": "Smartphone XYZ",
        "descricao": "Um smartphone de última geração com câmera de alta resolução",
        "preco": "2999.99"
    },
    {
        "id": "2",
        "nome": "Laptop ABC",
        "descricao": "Um laptop potente para trabalho e jogos",
        "preco": "4999.99"
    },
    {
        "id": "3",
        "nome": "Fone de Ouvido DEF",
        "descricao": "Fone de ouvido com cancelamento de ruído",
        "preco": "399.99"
    }
]





app = FastAPI()


@app.get("/") # Reqiest

def ola_mundo(): #Response
    return {"mensagem": "Olá Mundo!"}

@app.get("/produtos") # Request

def listar_produtos(): # Response
    return produtos

@app.get("/produtos/{id}") # Request
def buscar_produto(id: str):
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return {"Status":404,"mensagem": "Produto não encontrado"}