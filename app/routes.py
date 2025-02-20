from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .schema import ProdutosSchema
from .config import SessionLocal, get_db
from .model import Produto

router = APIRouter()



@router.get("/") # Reqiest
def ola_mundo(): #Response
    return {"mensagem": "Olá Mundo!"}

@router.get("/produtos", response_model=list[ProdutosSchema]) # Request


def listar_produtos(db: Session = Depends(get_db)): # Response
    return db.query(Produto).all()


@router.get("/produtos/{produto_id}", response_model=ProdutosSchema)
async def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    

# Rotas da API com lógica CRUD integrada
@router.post("/produtos", response_model=ProdutosSchema, status_code=201)
async def inserir_produto(produto: ProdutosSchema, db: Session = Depends(get_db)):
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@router.delete("/produtos/{produto_id}", response_model=ProdutosSchema)
async def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if produto:
        db.delete(produto)
        db.commit()
        return produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


@router.put("/produtos/{produto_id}", response_model=ProdutosSchema)
async def atualizar_produto(
    produto_id: int, produto_data: ProdutosSchema, db: Session = Depends(get_db)
):
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if db_produto:
        for key, value in produto_data.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit()
        db.refresh(db_produto)
        return db_produto
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado")