🏆 Exercício Prático: Sistema de Cadastro de Usuários (com DAO)

🎯 Objetivo

Criar um sistema de cadastro de usuários usando MVC + DAO, onde o usuário pode:

✅ Cadastrar um usuário (nome, e-mail, idade)

✅ Listar os usuários cadastrados

✅ Editar um usuário

✅ Excluir um usuário

---

📌 Regras do Sistema

•	O nome não pode estar vazio.

•	O e-mail não pode estar vazio e deve ser único.

•	A idade deve ser um número inteiro positivo.

•	Os dados devem ser armazenados em um arquivo JSON.

---

📂 Estrutura do Projeto

📦 seu_projeto/

┣ 📜 main.py → Arquivo principal para rodar o programa.

┣ 📜 model.py → Define a estrutura do usuário.

┣ 📜 dao.py → Gerencia o armazenamento dos usuários no JSON.

┣ 📜 controller.py → Faz as regras de validação e chama a DAO.

┗ 📜 view.py → Interage com o usuário (inputs e mensagens).

---

📝 Passo a Passo

1️⃣ Criar o model.py

	•	Criar uma classe Usuario com nome, email e idade.
	•	Criar um método dicionario() para converter um objeto Usuario em um dicionário.

2️⃣ Criar o dao.py

	•	Criar a classe UsuarioDAO com os métodos:
	•	carregar_usuarios() → Carrega a lista do JSON.
	•	salvar_usuarios(lista_de_usuarios) → Salva os usuários no JSON.

3️⃣ Criar o controller.py

	•	Criar a classe UsuarioController com os métodos:
	•	criar_usuario(nome, email, idade)
	•	listar_usuarios()
	•	editar_usuario(email, novo_nome, nova_idade)
	•	excluir_usuario(email)

4️⃣ Criar o view.py

	•	Criar a classe UsuarioView que chama o UsuarioController e exibe mensagens para o usuário.

5️⃣ Criar o main.py

	•	Criar um menu simples para testar o CRUD do sistema.