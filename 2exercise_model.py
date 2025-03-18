'''
📝 Exercício Prático - Cadastro de Usuários (com JSON)

Enunciado:

Crie um Model chamado Usuario com os seguintes atributos:
	•	nome (string)
	•	email (string)
	•	idade (inteiro, não pode ser negativa)

A classe deve ter:
	1.	__init__ → Inicializa os atributos e valida a idade.
	2.	__str__ → Retorna uma string amigável com os detalhes do usuário.

Crie também a classe CadastroUsuarios, que será responsável por gerenciar os usuários em um arquivo JSON.

A classe deve ter os seguintes métodos:
	•	adicionar_usuario(usuario): Adiciona um usuário à lista e salva no JSON.
	•	listar_usuarios(): Lê e retorna todos os usuários do JSON.

Se tentar criar um usuário com idade negativa, o programa deve exibir uma mensagem de erro e não permitir o cadastro.

📌 Objetivos:

✅ Praticar Model e validações.
✅ Implementar salvamento e leitura de dados em um arquivo JSON.
✅ Simular um pequeno sistema de cadastro de usuários.
'''

import json

class Usuario:
    def __init__(self, nome, email, idade):
        if not isinstance(idade, int):
            raise TypeError("A idade deve ser um número inteiro.")
        if idade < 0:
            raise ValueError("O valor não pode ser negativo.")
        
        self.nome = nome
        self.email = email
        self.idade = idade

    def __str__(self):
        return f"💁🏽 Cadastro de usuário!\nNome: {self.nome}\nEmail: {self.email}\nIdade: {self.idade}"
    
    def salvar(self):
        return {"nome": self.nome, "email": self.email, "idade": self.idade}
    
class CadastroUsuarios():

    @staticmethod
    def criar_usuario():
        try:
            with open('2exercise_model.json', 'r') as arq:
                usuarios = json.load(arq)
        except (FileNotFoundError, json.JSONDecodeError):
            usuarios = []

        nome = input('Digite o nome do usuário: ')
        email = input('Digite o email do usuário: ')
        while True:
            try:
                idade = int(input('Digite a idade do usuário: '))
                break
            except ValueError as e:
                print('Digite um valor válido.')

        usuario = Usuario(nome, email, idade).salvar()
        usuarios.append(usuario)

        with open('2exercise_model.json', 'w') as arq:
            json.dump(usuarios, arq, indent=4)

        print("\n✅ Usuário cadastrado com sucesso!")

    @staticmethod
    def listar_usuarios():
        try:
            # 🔹 Tenta abrir o arquivo JSON
            with open('2exercise_model.json', 'r') as arq:
                usuarios = json.load(arq)  # 🔹 Carrega os dados do JSON para uma lista

            # 🔹 Se a lista estiver vazia, exibe a mensagem e retorna
            if not usuarios:
                print('❌ Não existem usuários cadastrados.')
                return

            # 🔹 Exibe cada usuário de forma organizada
            print("\n📜 Lista de Usuários Cadastrados:\n")
            for i, usuario in enumerate(usuarios, start=1):
                print(f"🔹 Usuário {i}:")
                print(f"   Nome: {usuario['nome']}")
                print(f"   Email: {usuario['email']}")
                print(f"   Idade: {usuario['idade']}")
                print("-" * 30)

        except FileNotFoundError:
            print('❌ O arquivo de usuários não existe ainda.')
        except json.JSONDecodeError:
            print('❌ Erro ao ler o arquivo JSON (pode estar corrompido ou vazio).')
        

def menu():
    """Exibe um menu para o usuário interagir com o programa."""
    while True:
        print("📌 Menu:")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            CadastroUsuarios.criar_usuario()
        elif opcao == "2":
            CadastroUsuarios.listar_usuarios()
        elif opcao == "3":
            print("🚪 Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


# 🚀 Inicia o programa chamando o menu
menu()