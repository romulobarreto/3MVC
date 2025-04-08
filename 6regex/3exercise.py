'''
📝 Exercício 3 - Substituindo palavras em um texto

Enunciado:
Você recebeu um texto que contém a palavra "ruim", mas quer substituir todas as ocorrências por "bom".

Tarefa:
	1.	Use re.sub() para substituir todas as palavras "ruim" por "bom" no texto abaixo:
'''
texto = "Hoje o dia está ruim. Ontem também foi um dia ruim, mas amanhã será melhor."
'''
	2.	Exiba o texto modificado.

Dica:
	•	O método re.sub(padrao, substituto, texto) troca todas as ocorrências do padrão pelo substituto.
'''
import re

padrao = "ruim"

resultado = re.sub(padrao, "bom", texto)
print(resultado)