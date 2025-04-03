from view import *
from dao import UserDao

def menu():
    # Exibe o menu no terminal
    while True:
        print("\n📌 Menu:")
        print("1️⃣ - Cadastrar Usuário")
        print("2️⃣ - Listar Usuários")
        print("3️⃣ - Sair")

        opcao = input("\nEscolhe uma das opções: ").strip()
        
        if opcao == "1":
            UserView.cadastrar_usuario()
        elif opcao == "2":
            UserView.listar_usuarios()
            usuarios = UserDao.carregar_usuarios()
            if not usuarios:
                continue
            print("\n1️⃣ - Detalhar Usuário")
            print("2️⃣ - Excluir Usuário")
            print("3️⃣ - Editar Usuário")
            print("4️⃣ - Voltar")
            opcao1 = input("\nEscolhe uma das opções: ").strip()
            
            if opcao1 == "1":
                UserView.detalhar_usuario()
            elif opcao1 == "2":
                UserView.excluir_usuario()
            elif opcao1 == "3":
                UserView.editar_usuario()
            elif opcao1 == "4":
                continue
            else:
                print("⚠️ Opção inválida! Tente novamente.\n")


        elif opcao == "3":
            print("🚪 Saindo do programa...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")



if __name__ == "__main__":
    menu()