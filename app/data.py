
from typing import List, Dict

class Produtos:
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

    def listar_produtos(self):
        return self.produtos
    
    def buscar_produto(self,id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
            
    def cadastrar_produto(self, produto):
        self.produtos.append(produto)
        return produto