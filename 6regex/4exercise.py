'''
📝 Exercício 4 - Censurando palavras proibidas

Enunciado:
Imagine que você está criando um sistema para um fórum online e quer censurar palavras inapropriadas.

Tarefa:
	1.	No texto abaixo, substitua as palavras "bobo", "chato" e "feio" por "***".
	2.	Exiba o texto modificado.
'''
texto = "Esse jogo é muito bobo! Esse filme é chato e o final é feio."
'''
Dica:
	•	O re.sub() aceita um padrão mais complexo, onde você pode substituir várias palavras ao mesmo tempo usando | (OU).
'''

import re

padrao = "bobo|chato|feio"

resultado = re.sub(padrao, "***", texto)

print(resultado)