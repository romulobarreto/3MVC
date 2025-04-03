from controller import *

class UserView():

    @staticmethod
    def cadastrar_usuario():
        # Pede os inputs
        nome = input("\nDigite o nome do usuário: ").strip().lower()
        email = input("\nDigite o email do usuário: ").strip().lower()
        try:
            idade = int(input("\nDigite a idade do usuário: ").strip())
        except ValueError:
            print("⚠️ Idade precisa ser um número inteiro.")
            return
        
        # Cria o usuário
        sucesso, mensagem = UserController.cadastrar_usuario(nome, email, idade)
        print(mensagem)


    @staticmethod
    def listar_usuarios():
        # Chama a função do controller:
        sucesso, mensagem = UserController.listar_usuarios()

        # Exibe o resultado vindo do controller
        print(mensagem)


    @staticmethod
    def detalhar_usuario():
        # Captura o input
        usuario = input("\nDigite o nome do usuário que deseja detalhar: ").strip().lower()

        # Chama a função de detalhar usuário
        sucesso, mensagem = UserController.detalhar_usuario(usuario)

        # Exibe resultado vindo do controller
        print(mensagem)

    
    @staticmethod
    def excluir_usuario():
        # Captura o input
        usuario = input("\nDigite o email do usuário que deseja excluir: ").strip().lower()

        # Chama a função de detalhar usuário
        sucesso, mensagem = UserController.excluir_usuario(usuario)

        # Exibe resultado vindo do controller
        print(mensagem)


    
    @staticmethod
    def editar_usuario():
        # Carregar lista
        usuarios = UserDao.carregar_usuarios()
        
        editar = input('Digite o email do usuário que deseja editar: ').strip().lower()

        # Valida se o nome está na lista
        if not editar:
            print(f'⚠️ O email digitado não pode ser vazio.')
            return
            
        usuario_lista = None
        for usuario in usuarios:
            if usuario['email'] == editar:
                usuario_lista = usuario
                break
            
        if not usuario_lista:
            print(f"❌ O usuário '{editar}' não está na lista.\n")
            return
        
        # Mostra detalhes do usuário escolhido
        print(f"\n📋 Detalhes do usuário:\nNome: {usuario_lista['nome']}\nEmail: {usuario_lista['email']}\nIdade: {usuario_lista['idade']}\n")

        # Solicita a chave ao usuário
        chave = input("Escolha a opção que deseja editar:\nNome\nEmail\nIdade\n").strip().lower()

        # Valida se a chave existe
        if not chave in usuario_lista:
            print(f'⚠️ A opção {chave} é inválida.')
            return

        # Input com o valor atualizado
        nova_info = None
        if chave == "nome":
            nome = input('Digite o novo nome do usuário (ou pressione Enter para manter o mesmo): ').strip().lower()
            nova_info = nome if nome else usuario_lista['nome']
            nome = nova_info
            email = usuario_lista['email']
            idade = usuario_lista['idade']

        elif chave == "email":
            email = input('Digite o novo email (ou pressione Enter para manter o mesmo): ').strip().lower()
            nova_info = email if email else usuario_lista['email']
            nome = usuario_lista['nome']
            email = nova_info
            idade = usuario_lista['idade']

        elif chave == "idade":
            try:
                idade = int(input('Digite a nova idade (ou pressione Enter para manter o mesmo): ').strip())
                nova_info = idade
                nome = usuario_lista['nome']
                email = usuario_lista['email']
                idade = nova_info
            except ValueError:
                nome = usuario_lista['nome']
                email = usuario_lista['email']
                idade = usuario_lista['idade']
            
        
        sucesso, mensagem = UserController.editar_usuario(nome, email, idade, usuario_lista)
        if sucesso:
            print(mensagem)
            print(f"✅ {editar} teve o dado de {chave} atualizado:\nDe: {usuario_lista[chave]}\nPara: {nova_info}.")
        else:
            print(mensagem)