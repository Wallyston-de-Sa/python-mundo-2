# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

# Contadores
menores = 0
maiores = 0

# Entrada de dados e processamento
for c in range (1, 8):
    nascimento = int(input('Digite o ano em que a {}º pessoa nasceu: '.format(c)))
    idade = date.today().year - nascimento
    if idade > 18:
        maiores += 1
    else:
        menores += 1

# Saída de resultados
print('{} pessoas são menores de 18 anos.'.format(menores))
print('{} pessoas são maiores de 18 anos.'.format(maiores))