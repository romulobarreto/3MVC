'''
🏆 Exercício 1: Encontrando uma Palavra em um Texto

🎯 Objetivo:

Usar regex para verificar se uma palavra específica está presente em um texto usando re.search().

📌 O que você precisa fazer:
	1.	Criar uma string qualquer, como um texto curto.
	2.	Criar uma regex para buscar uma palavra específica dentro dessa string.
	3.	Usar re.search() para verificar se a palavra foi encontrada.
	4.	Exibir uma mensagem informando se a palavra foi encontrada ou não.

🔍 Dicas:
	•	re.search(padrao, texto) verifica se o padrão aparece em qualquer parte do texto.
	•	Se encontrar, re.search() retorna um objeto match, senão retorna None.
	•	Para testar, pode usar um texto como "Hoje o dia está ensolarado e bonito" e buscar "dia".
'''

import re

texto = "Hoje o dia está ensolarado e bonito"

padrao = "dia"

resultado = re.search(padrao, texto)

if resultado:
    print(f"Encontrado: {resultado.group()}")
    print(f"Posição: {resultado.span()}")
    print(f"Início: {resultado.start()}")
    print(f"Final: {resultado.end()}")
else:
    print("Não encontrado.")
