from view import ProdutoView

def menu():
    # Exibe o menu para o usuário
    while True:
        print("\n📌 Menu:")
        print("1- Listar produtos")
        print("2- Cadastrar produto")
        print("3- Sair")

        opcao = input("\nEscolha uma das opções: ").strip()

        if opcao == "1":
            #Listar produtos
            ProdutoView.listar_produtos()

            #Sub-menu
            print("1.1- Detalhar produto")
            print("1.2- Excluir produto")
            print("1.3- Editar produto")
            print("1.4- Voltar")

            opcao1 = input("\nEscolha uma das opções: ").strip()

            if opcao1 == "1.1":
                ProdutoView.detalhar_produto()
            elif opcao1 == "1.2":
                ProdutoView.excluir_produto()
            elif opcao1 == "1.3":
                ProdutoView.editar_produto()
            elif opcao1 == "1.4":
                continue
            else:
                print("⚠️ Opção inválida! Tente novamente.\n")

        elif opcao == "2":
            ProdutoView.cadastrar_produto()

        elif opcao == "3":
            print("🚪 Saindo do programa...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    menu()