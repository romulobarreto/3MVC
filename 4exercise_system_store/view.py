from controller import ProdutoController

class ProdutoView():

    @staticmethod
    def listar_produtos():
        # Carregar produtos
        produtos = ProdutoController.carregar_produtos()

        if not produtos:
            print("📦🚫 Sem produtos cadastrados.\n")
            return

        # Listar nome dos produtos
        print("📦 Lista de produtos:")
        for index, produto in enumerate(produtos, start=1):
            print(f"{index}°: {produto['nome'].title()}")
        print("--------------------\n")

    
    @staticmethod
    def detalhar_produto():

        # Carregar produtos
        produtos = ProdutoController.carregar_produtos()

        if not produtos:
            print("📦🚫 Sem produtos cadastrados.\n")
            return
        
        # Input e tratamento do input
        while True:
            produto_detalhado = input('Digite o nome do produto que deseja detalhar: ').lower().strip()

            if not produto_detalhado:
                print('⚠️ O nome digitado é inválido.')
                continue
            else:
                break

        # Encontrar o produto e detalhar
        detalhar = None
        for produto in produtos:
            if produto['nome'] == produto_detalhado:
                detalhar = produto
                break

        if detalhar:
            print(f"📋 Detalhes do produto:\nNome: {detalhar['nome']}\nPreço: R${detalhar['preco']:.2f}\nEstoque: {detalhar['quantidade']}")
        else:
            print(f"{produto_detalhado.title()} não faz parte da lista de produtos.")


    @staticmethod
    def cadastrar_produto():
        # Carregar produtos
        produtos = ProdutoController.carregar_produtos()

        if not produtos:
            print("📦🚫 Sem produtos cadastrados.\n")
            return

        # Coletar produto
        while True:
            nome = input('Digite o nome do produto: ').strip().lower()

            # Valida se o nome é válido
            if not nome:
                print('⚠️ O nome digitado é inválido.')
                continue

            # Validar se já existe
            produto_existe = False
            for produto in produtos:
                if produto['nome'] == nome:
                    produto_existe = True
            
            if produto_existe:
                print(f"⚠️ O produto '{nome}' já está cadastrado.\n")
                continue
            else:
                break

        # Coletar preço
        while True:  
            try:
                preco = float(input('Digite o valor do produto: R$ '))

                if not preco:
                    print("⚠️ O preço não pode ser vazio.\n")
                    continue

                if preco < 0:
                    print("⚠️ O valor não pode ser negativo.\n")
                    continue
                break
            except ValueError:
                print('⚠️ O valor digitado precisa ser numérico.\n')

        # Coletar quantidade em estoque
        while True:
            try:
                quantidade = int(input('Digite a quantidade em estoque do produto: '))

                if not quantidade:
                    print("⚠️ A quantidade não pode ser vazia.\n")
                    continue

                if quantidade < 0:
                    print("⚠️ A quantidade em estoque não pode ser negativa.\n")
                    continue
                break
            except ValueError:
                print('⚠️ O valor digitado precisa ser numérico.\n')

        # Criar o novo produto
        ProdutoController.criar_produto(nome, preco, quantidade)
        print(f"✅ Produto '{nome}' cadastrado com sucesso!\n")
        

    @staticmethod
    def excluir_produto():
        # Carregar produtos
        produtos = ProdutoController.carregar_produtos()

        if not produtos:
            print("📦🚫 Sem produtos cadastrados.\n")
            return

        # Coletar produto para excluir
        while True:
            excluir = input('Digite o nome do produto que deseja excluir: ').strip().lower()

            # Valida se o nome é válido
            if not excluir:
                print(f'⚠️ O nome digitado é inválido.')
                return

            # Validar se já existe
            dicionario = None
            for produto in produtos:
                if produto['nome'] == excluir:
                    dicionario = produto
            
            if dicionario:
                ProdutoController.excluir_produto(dicionario)
                print(f"✅ O produto '{excluir}' foi removido da lista.\n")
                return
            else:
                print(f"❌ O produto '{excluir}' não está na lista.\n")
                return


    @staticmethod
    def editar_produto():
        # Carregar lista
        produtos = ProdutoController.carregar_produtos()

        if not produtos:
            print("📦🚫 Sem produtos cadastrados.\n")
            return
        
        while True:
            editar = input('Digite o nome do produto que deseja editar: ').strip().lower()

            # Valida se o nome está na lista
            if not editar:
                print(f'⚠️ O nome digitado é inválido.')
                return
            
            produto_lista = None
            for produto in produtos:
                if produto['nome'] == editar:
                    produto_lista = produto
                    break
            
            if not produto_lista:
                print(f"❌ O produto '{editar}' não está na lista.\n")
                return
            
            print(f"\n📋 Detalhes do produto:\nNome: {produto_lista['nome']}\nPreço: R${produto_lista['preco']:.2f}\nEstoque: {produto_lista['quantidade']}\n")
            break

        # Valida se a chave existe
        while True:
            chave = input("Escolha a opção que deseja editar:\nNome\nPreço\nQuantidade\n").strip().lower().replace("ç", "c")

            if not chave in produto_lista:
                print(f'⚠️ A opção {chave} é inválida.')
                continue
            else:
                break

        # Input com o valor atualizado
        nova_info = None
        if chave == "nome":
            nome = input('Digite o novo nome do produto (ou pressione Enter para manter o mesmo): ').strip().lower()
            nova_info = nome if nome else produto_lista['nome']

        elif chave == "preco":
            while True:
                preco = input('Digite o novo preço (ou pressione Enter para manter o mesmo): ').strip()
                if not preco:
                    nova_info = produto_lista['preco']
                    break
                try:
                    nova_info = float(preco)
                    if nova_info < 0:
                        print("⚠️ O valor não pode ser negativo.\n")
                        continue
                    break
                except ValueError:
                    print("⚠️ O valor precisa ser numérico.\n")

        elif chave == "quantidade":
            while True:
                quantidade = input('Digite a nova quantidade (ou pressione Enter para manter a mesma): ').strip()
                if not quantidade:
                    nova_info = produto_lista['quantidade']
                    break
                try:
                    nova_info = int(quantidade)
                    if nova_info < 0:
                        print("⚠️ A quantidade não pode ser negativa.\n")
                        continue
                    break
                except ValueError:
                    print("⚠️ O valor precisa ser um número inteiro.\n")
        
        ProdutoController.editar_produto(produtos)
        valor_formatado = f"R${nova_info:.2f}" if chave == "preco" else nova_info
        print(f"✅ {editar.title()} teve o dado de {chave} atualizado para: {valor_formatado}.")