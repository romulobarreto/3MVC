'''
📌 O que é a View no MVC?

A View (ou “visão”) é a camada responsável pela interface com o usuário. Ela exibe as informações vindas do Model e recebe comandos do usuário, que depois são enviados para o Controller.

🔹 Função principal da View:
✅ Mostrar os dados de forma organizada (pode ser no terminal, HTML, app, etc.)
✅ Capturar as interações do usuário (inputs, cliques, comandos, etc.)
✅ Não deve conter regras de negócio (as regras ficam no Model)

🛠 Estrutura básica do MVC:

📌 Model → Gerencia os dados e regras de negócio
📌 View → Exibe informações e captura interações
📌 Controller → Coordena a comunicação entre Model e View





🖥 Exemplo 1: Sistema de Usuários (View no Terminal)

Vamos continuar com o exemplo de cadastro de usuários que fizemos antes. Suponha que o Model já está pronto (Usuario), agora vamos criar a View para exibir os usuários no terminal.
'''
# 📌 Model (Representa os dados)
class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Idade: {self.idade}"

# 📌 View (Mostra os usuários na tela)
class UsuarioView:
    @staticmethod
    def exibir_usuario(usuario):
        print("\n📌 Dados do Usuário:")
        print(f"Nome: {usuario.nome}")
        print(f"Email: {usuario.email}")
        print(f"Idade: {usuario.idade}")
    
    @staticmethod
    def listar_usuarios(usuarios):
        if not usuarios:
            print("\n❌ Nenhum usuário cadastrado.")
            return
        print("\n📜 Lista de Usuários:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario.nome} - {usuario.email} - {usuario.idade} anos")

# 📌 Saída esperada no terminal:
'''
📌 Dados do Usuário:
Nome: João Silva
Email: joao@email.com
Idade: 30

📜 Lista de Usuários:
1. João Silva - joao@email.com - 30 anos
2. Maria Souza - maria@email.com - 25 anos

🔹 O que a View fez?
✅ Recebeu dados do Model e os exibiu no terminal
✅ Formatou as informações para melhor visualização
✅ Não fez validações ou cálculos (essas regras são do Model)





🎯 Resumo da View

📌 A View não toma decisões nem processa dados, ela apenas exibe informações.
📌 Pode ser um menu no terminal, uma página HTML ou até uma API JSON.
📌 Ela recebe os dados do Controller, que pegou do Model.
'''