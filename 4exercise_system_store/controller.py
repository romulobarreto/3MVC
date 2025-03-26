from model import Produto
import json

class ProdutoController():

    @staticmethod
    def carregar_produtos():
        # Carrega os dicionários de dentro do JSON
        try:
            with open("products_db.json", "r") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    
    @staticmethod
    def salvar_produtos(produtos):
        # Salva as alterações no JSON
        try:
            with open("products_db.json", "w") as arq:
                json.dump(produtos, arq, indent=4)
        except Exception as e:
            print("⚠️ Erro ao salvar os dados no arquivo.\n")
    

    @staticmethod
    def criar_produto(nome, preco, quantidade):
        # Carregar lista de produtos
        produtos = ProdutoController.carregar_produtos()

        # Criar novo produto
        novo_produto = Produto(nome, preco, quantidade)

        # Salvar produto
        produtos.append(novo_produto.dicionario())
        ProdutoController.salvar_produtos(produtos)

    
    @staticmethod
    def excluir_produto(dicionario):
        # Carregar produtos
        produtos = ProdutoController.carregar_produtos()

        # Excluir dicionário do produto da lista
        produtos.remove(dicionario)

        # Salvar lista atualizada
        ProdutoController.salvar_produtos(produtos)

    
    @staticmethod
    def editar_produto(produtos):
        # Salvar lista editada
        ProdutoController.salvar_produtos(produtos)