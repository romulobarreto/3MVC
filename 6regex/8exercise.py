'''
📝 Exercício 2 - Encontrando palavras específicas em um texto

📌 Enunciado:

Você recebeu um texto e precisa encontrar todas as palavras que começam com a letra “p” (maiúscula ou minúscula).

🎯 Tarefas:
	1.	Use re.findall() para capturar todas as palavras que começam com “p” ou “P”.
	2.	Exiba a lista de palavras encontradas.

💡 Dicas:
	•	O \b indica fronteira de palavra.
	•	A classe de caracteres [Pp] pode te ajudar a capturar maiúsculas e minúsculas.
	•	O \w+ captura o restante da palavra.

📜 Texto para testar:
'''
texto = "O Pedro pediu uma pizza para o jantar. Porém, preferiu pedir pastel depois."

import re

padrao_p = r"\b[Pp]\w*"

captura = re.findall(padrao_p, texto)
print(captura)