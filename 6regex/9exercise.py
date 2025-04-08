'''
📝 Exercício 3 - Encontrando valores monetários

📌 Enunciado:
Você recebeu um texto que contém valores em reais (R$) escritos de diferentes formas. Seu objetivo é capturar todos os valores presentes no texto.

📜 Texto para análise:
'''
texto = "O produto custa R$ 129,99. Outra opção é pagar R$59,90 ou até mesmo R$ 1.000,00 à vista."
'''
🎯 Tarefas:
	1.	Usar regex para encontrar todos os valores em reais no texto.
	2.	Capturar valores com diferentes formatações, como:
	•	R$ 129,99
	•	R$59,90
	•	R$ 1.000,00
	3.	Exibir os valores encontrados.

💡 Dicas:
	•	O valor sempre começa com “R$” (com ou sem espaço depois).
	•	Pode haver pontos para separar milhares (1.000,00).
	•	O valor sempre tem duas casas decimais após a vírgula.
	•	Você pode usar grupos de captura para pegar as partes separadamente.
'''
import re

padrao = r"\b[R]?\s\w*"

procura = re.findall(padrao, texto)

print(procura)