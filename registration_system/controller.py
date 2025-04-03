from dao import *
from model import User
import re

class UserController():

    @staticmethod
    def validar_dados(nome, email, idade, email_atual=None):
        # Forma um padrão de email
        padrao_email = r"^[\w]+([\.-]?[\w]+)*@[\w-]+(\.[\w-]+)+$"

        # Carregar lista de usuários
        usuarios = UserDao.carregar_usuarios()

        # Validação dos dados recebidos
        if not nome:
            return False, "⚠️ O nome não pode estar vazio."
        
        if not email:
            return False, "⚠️ O email não pode estar vazio."
        
        if email != email_atual and any(usuario['email'] == email for usuario in usuarios):
            return False, "🚫 Usuário já cadastrado."
        
        if not re.match(padrao_email, email):
            return False, "⚠️ O email está fora do padrão de criação."
        
        if idade < 18:
            return False, "🚫 Usuário menor de idade."
        
        return True, "✅ Dados aprovados."
    
    @staticmethod
    def cadastrar_usuario(nome, email, idade):

        # Carregar lista de usuários
        usuarios = UserDao.carregar_usuarios()

        # Validação dos dados recebidos
        sucesso, mensagem = UserController.validar_dados(nome, email, idade)
        if not sucesso:
            return False, mensagem
    
        # Criar o novo usuário
        usuario = User(nome, email, idade)

        # Adicionar à lista e salvar
        usuarios.append(usuario.formatar_dict())
        sucesso = UserDao.salvar_usuarios(usuarios)  # Captura o retorno da DAO

        if sucesso:
            return True, "✅ Usuário cadastrado com sucesso."
        else:
            return False, "⚠️ Erro ao salvar o usuário no banco de dados."


    
    @staticmethod
    def listar_usuarios():
        # Carregar usuários
        usuarios = UserDao.carregar_usuarios()

        # Verificar se existe usuário cadastrado
        if not usuarios:
            return False, "\n⚠️ A lista de usuários está vazia, faça um cadastro!"
        
        # Listar usuários
        lista_formatada = "\n📋 Lista de usuários cadastrados:\n"
        for index, usuario in enumerate(usuarios, start=1):
            lista_formatada += f"{index}°: {usuario['nome'].title()}\n"
        lista_formatada += "---------------------------"

        return True, lista_formatada
    

    @staticmethod
    def detalhar_usuario(usuario):
        # Carregar usuários cadastrados
        usuarios = UserDao.carregar_usuarios()
        
        # Valida se o usuário está na lista
        for index, user in enumerate(usuarios, start=1):
            if index == usuario:
                return True, f"🗂️ Dados detalhados:\nNome: {user['nome'].title()}\nEmail: {user['email']}\nIdade: {user['idade']}"

        return False, "⚠️ O usuário não está na lista."
    
    @staticmethod
    def excluir_usuario(usuario):
        # Carregar usuários cadastrados
        usuarios = UserDao.carregar_usuarios()

        # Validação de usuário digitado
        if not usuario:
            return False, "⚠️ O nome não pode estar vazio."
        
        # Valida se o usuário está na lista
        dicionario_usuario = None
        for user in usuarios:
            if user['email'] == usuario:
                dicionario_usuario = user
                break
        
        if not dicionario_usuario:
            return False, "⚠️ O nome não está na lista."
        
        # Remove o dicionario do usuário escolhido da base
        usuarios.remove(dicionario_usuario)

        # Salva a nova lista de usuários na base
        UserDao.salvar_usuarios(usuarios)
        return True, "✅ Usuário deletado com sucesso."
    


    @staticmethod
    def editar_usuario(nome, email, idade, usuario_lista):
        # Valida os dados
        sucesso, mensagem = UserController.validar_dados(nome, email, idade, usuario_lista['email'])
        if not sucesso:
            return False, mensagem

        # Carrega lista de usuários
        usuarios = UserDao.carregar_usuarios()

        # Encontra o usuário na lista e edita diretamente
        for usuario in usuarios:
            if usuario['email'] == usuario_lista['email']:  # Usa o email como identificador único
                usuario['nome'] = nome
                usuario['email'] = email
                usuario['idade'] = idade
                break

        # Salva a lista editada no JSON
        sucesso = UserDao.salvar_usuarios(usuarios)

        if sucesso:
            return True, "✅ Usuário editado com sucesso."
        else:
            return False, "⚠️ Erro ao salvar a alteração no banco de dados."