'''
📂 O que é DAO (Data Access Object)?

DAO (Data Access Object) é um padrão de design que separa a lógica de acesso a dados do resto da aplicação. Ele é responsável exclusivamente por salvar, carregar, atualizar e excluir dados.

Ou seja, tudo que envolve acessar um banco de dados (ou um arquivo JSON, no seu caso), fica dentro da DAO. Assim, o resto do sistema não precisa se preocupar com “como” os dados são armazenados.





🎯 Por que usar DAO?

✅ Separação de responsabilidades → Deixa o código mais organizado e fácil de manter.
✅ Facilidade para mudar o armazenamento → Hoje usamos JSON, mas no futuro, se migrarmos para um banco de dados, só a DAO precisará mudar.
✅ Reutilização de código → Evita repetição de código, pois todas as operações de dados ficam centralizadas na DAO.
✅ Facilita testes → Podemos testar a lógica da aplicação sem depender de como os dados são armazenados.





🏗️ Como a DAO se encaixa no MVC?

No padrão MVC, o DAO se encaixa da seguinte forma:

🔹 Model (Modelo) → Define a estrutura dos dados (por exemplo, a classe Produto).
🔹 DAO (Data Access Object) → Manipula os dados no armazenamento (JSON, banco de dados, etc.).
🔹 Controller (Controlador) → Regras de negócio, validações e chamadas para a DAO.
🔹 View (Visão) → Interface com o usuário (exibe mensagens, recebe inputs, etc.).

👉 A DAO só se preocupa em acessar e manipular os dados, enquanto o Controller toma decisões e a View interage com o usuário.





📝 Exemplo de DAO (usando JSON)

Vamos imaginar que temos um sistema de produtos.

📌 Antes, o Controller fazia tudo sozinho, carregando e salvando o JSON.
📌 Agora, criamos uma DAO para cuidar disso!
'''
#🔹 Model (model.py)
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def dicionario(self):
        return {"nome": self.nome, "preco": self.preco, "quantidade": self.quantidade}
    
# 🔹 DAO (dao.py)
import json

class ProdutoDAO:

    @staticmethod
    def carregar_produtos():
        """Carrega os produtos do arquivo JSON."""
        try:
            with open("products_db.json", "r") as arq:
                return json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def salvar_produtos(produtos):
        """Salva a lista de produtos no arquivo JSON."""
        try:
            with open("products_db.json", "w") as arq:
                json.dump(produtos, arq, indent=4)
            return True, "Dados salvos com sucesso!"
        except Exception as e:
            return False, "Erro ao salvar os dados."
        
# 🔹 Controller (controller.py)
class ProdutoController:

    @staticmethod
    def criar_produto(nome, preco, quantidade):
        """Cria um novo produto após validar os dados."""
        produtos = ProdutoDAO.carregar_produtos()

        # Verifica se já existe um produto com o mesmo nome
        if any(p["nome"] == nome for p in produtos):
            return False, "Produto já cadastrado."

        novo_produto = Produto(nome, preco, quantidade)
        produtos.append(novo_produto.dicionario())

        return ProdutoDAO.salvar_produtos(produtos)

    @staticmethod
    def listar_produtos():
        """Retorna a lista de produtos."""
        produtos = ProdutoDAO.carregar_produtos()
        return produtos if produtos else []
    
# 🔹 View (view.py)

class ProdutoView:

    @staticmethod
    def cadastrar_produto():
        """Coleta dados e chama o Controller para criar um novo produto."""
        nome = input("Digite o nome do produto: ").strip().lower()

        try:
            preco = float(input("Digite o preço do produto: R$ "))
            quantidade = int(input("Digite a quantidade em estoque: "))
        except ValueError:
            print("⚠️ Entrada inválida! O preço deve ser um número e a quantidade um inteiro.\n")
            return

        sucesso, mensagem = ProdutoController.criar_produto(nome, preco, quantidade)

        if sucesso:
            print(f"✅ {mensagem}")
        else:
            print(f"❌ {mensagem}")




'''
🚀 Conclusão

🔹 A View coleta os dados do usuário e passa para o Controller.
🔹 O Controller faz as validações e chama a DAO para salvar no JSON.
🔹 A DAO é a única parte do código que sabe onde e como os dados são armazenados.

Isso deixa nosso código mais limpo, organizado e fácil de modificar no futuro! 😃
'''