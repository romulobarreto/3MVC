'''
🚀 Próximo Exercício - Validando e formatando números de telefone

📌 Enunciado:
Você recebeu uma lista de números de telefone que podem estar escritos de formas diferentes, como:
	•	(51) 98765-4321
	•	51987654321
	•	51 98765 4321
Seu objetivo é capturar o DDD e o número e reformatá-los corretamente no padrão (XX) XXXXX-XXXX.

🎯 Tarefas:
	1.	Usar regex para encontrar e capturar o DDD e o número.
	2.	Independente do formato original, reformatar os números corretamente para (XX) XXXXX-XXXX.
	3.	Exibir a lista formatada.

💡 Dicas:
	•	O DDD sempre tem 2 dígitos e aparece no início.
	•	O número pode ter 9 dígitos (começando com 9) ou 8 dígitos.
	•	Caracteres como espaços, traços e parênteses podem variar, então você precisa lidar com isso.
	•	Você pode usar re.sub() para transformar qualquer formato no padrão desejado!

📌 Lista de telefones para testar:
'''
import re

# Regex corrigida:
padrao = r"\(?(\d{2})\)?[\s-]?(\d{4,5})[\s-]?(\d{4})"

telefones = [
    "(51) 98765-4321",
    "51987654321",
    "51 98765 4321",
    "(11) 91234-5678",
    "11912345678",
    "11 91234 5678",
    "71-99876-5432",
    "(21)8888-7777"
]

for telefone in telefones:
    resultado = re.findall(padrao, telefone)
    if resultado:
        ddd, parte1, parte2 = resultado[0]  # Pegamos o primeiro match
        telefone_formatado = f"({ddd}) {parte1}-{parte2}"
        print(telefone_formatado)