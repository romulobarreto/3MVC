import re

'''
📝 Exercício 2 - Encontrando todas as palavras específicas

Enunciado:
Imagine que você está analisando um texto e quer encontrar todas as ocorrências da palavra "dia", incluindo variações como "dia" dentro de outras palavras, como "dias" ou "bomdia".

Tarefa:
	1.	Utilize re.findall() para encontrar todas as ocorrências do padrão "dia" no texto abaixo:
'''
texto = "O dia está lindo! Amanhã será outro dia. Bomdia para todos os dias!"
'''
	2.	Exiba a lista de palavras encontradas.

Dicas:
	•	O método re.findall(padrao, texto) retorna uma lista com todas as ocorrências do padrão.
	•	Ele não retorna um objeto Match, apenas os textos encontrados.
'''

padrao = "dia"

resultado = re.findall(padrao, texto)

print(resultado)