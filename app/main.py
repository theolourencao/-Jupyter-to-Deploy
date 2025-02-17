from fastapi import FastAPI
from .schema import ProdutosSchema
from .data import Produtos

app = FastAPI()
lista_de_produtos = Produtos()

@app.get("/") # Reqiest
def ola_mundo(): #Response
    return {"mensagem": "Olá Mundo!"}

@app.get("/produtos", response_model=list[ProdutosSchema]) # Request

def listar_produtos(): # Response
    return lista_de_produtos.listar_produtos()


@app.get("/produtos/{id}", response_model =ProdutosSchema) # Request
def buscar_produto(id: str):
    return lista_de_produtos.buscar_produto(id)

@app.post("/produtos", response_model=ProdutosSchema)
def cadastrar_produto(produto: ProdutosSchema):
    return lista_de_produtos.cadastrar_produto(produto.model_dump())