'''
📝 Exercício 1: Capturando diferentes tipos de caracteres

Vamos começar com um exercício simples para praticar esses conceitos.

🚀 Enunciado:

Você recebeu um texto e precisa extrair diferentes tipos de caracteres. Use regex para capturar:
✅ Todos os números (usando \d)
✅ Todas as palavras (usando \w)
✅ Todos os espaços (usando \s)
✅ Todos os caracteres especiais (usando . e negando outras categorias)

🔍 Texto para teste:
'''
texto = "O preço do produto é R$ 129,99 e ele estará disponível dia 12/04/2025!"
'''
💡 Dica:
	•	Use re.findall() para encontrar cada tipo de caractere separadamente.
	•	Você pode usar [^...] para negar certas categorias (por exemplo, capturar só símbolos).
'''

import re

padrao_numero = r"\d"
numeros = re.findall(padrao_numero, texto)
print(numeros)

padrao_letra = r"\w"
letras = re.findall(padrao_letra, texto)
print(letras)

padrao_espaco = r"\s"
espaco = re.findall(padrao_espaco, texto)
print(espaco)

padrao_caracter = r"[^\w\s,/]"
caracter = re.findall(padrao_caracter, texto)
print(caracter)