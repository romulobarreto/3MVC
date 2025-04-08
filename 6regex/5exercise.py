'''
📝 Exercício 5 - Extraindo datas de um texto

Enunciado:
Você recebeu um texto com algumas datas no formato dd/mm/aaaa e precisa extraí-las.

Tarefa:
	1.	Usando re.findall(), capture todas as datas do texto abaixo:
'''
texto = "As reuniões ocorreram em 12/05/2023, 23/08/2022 e 07/11/2021."
'''
2.	Exiba todas as datas encontradas.

Dica:
	•	Você pode criar um padrão para datas usando:
	•	\d{2} para dois dígitos (dia/mês)
	•	\d{4} para quatro dígitos (ano)
	•	Use parênteses () para capturar cada parte separadamente!
'''

import re

padrao = r"\d{2}/\d{2}/\d{4}"

resultado = re.findall(padrao, texto)

print(resultado)

'''
🔥 Desafio extra:

Altere seu regex para capturar três grupos:
	1.	Dia
	2.	Mês
	3.	Ano

E exiba cada um separadamente.

Dica: Se re.findall() for usado com grupos de captura, ele retorna uma lista de tuplas!

Tenta aí e me diz o que acontece! 🚀
'''

padrao2 = r"(\d{2})/(\d{2})/(\d{4})"

resultado2 = re.findall(padrao2, texto)

print(resultado2)

for dia, mes, ano in resultado2:
    print(f"Dia: {dia}\nMês: {mes}\nAno: {ano}")