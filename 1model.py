'''
📌 O que é Model no MVC?

No padrão MVC (Model-View-Controller), o Model é a camada responsável por lidar com os dados da aplicação. Ele representa os objetos e regras de negócio, interage com o banco de dados (se houver um) e processa a lógica principal do sistema.

🔹 Principais responsabilidades do Model:
	1.	Armazenar e manipular dados (mesmo sem um banco de dados).
	2.	Aplicar regras de negócio (validações, cálculos, etc.).
	3.	Fornecer dados para o Controller, que depois repassa para a View.
'''

# 📌 Exemplo 1 - Sistema de Cadastro de Produtos (Sem Banco de Dados):
# Vamos criar um Model para gerenciar um catálogo de produtos sem banco de dados, usando apenas uma lista na memória.
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'Produto: {self.nome} | Preço: R$ {self.preco:.2f}'


class Catalogo:
    def __init__(self):
        self.produtos = []  # Armazena os produtos em uma lista

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        return self.produtos


# Criando um catálogo e adicionando produtos (simulando um Model)
catalogo = Catalogo()
catalogo.adicionar_produto(Produto("Notebook", 3500))
catalogo.adicionar_produto(Produto("Mouse", 150))

# Listando os produtos
for produto in catalogo.listar_produtos():
    print(produto)
'''
📌 O que acontece aqui?
	•	Criamos um Model simples para armazenar produtos (Produto) e um catálogo (Catalogo).
	•	O Catalogo age como um repositório de produtos.
	•	O método listar_produtos() retorna os produtos cadastrados.
'''





# 📌 Exemplo 2 - Model com Validações:
# Vamos adicionar uma regra de negócio no Model: o preço do produto não pode ser negativo.
class Produto:
    def __init__(self, nome, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo!")
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'Produto: {self.nome} | Preço: R$ {self.preco:.2f}'


# Testando a validação
try:
    p1 = Produto("Teclado", 200)
    print(p1)

    p2 = Produto("Monitor", -500)  # Vai gerar um erro
    print(p2)
except ValueError as e:
    print(f"Erro ao criar produto: {e}")
'''
📌 Destaques:
	•	Se alguém tentar cadastrar um produto com preço negativo, o Model impede isso.
	•	A regra de negócio fica dentro da classe, garantindo que ninguém crie produtos inválidos.
'''