# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
menores = 0
maiores = 0

for c in range (7):
    nascimento = int(input('Digite o ano do seu nascimento: '))
    idade = date.today().year - nascimento
    if idade > 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são menores de 18 anos.'.format(menores))
print('{} pessoas são maiores de 18 anos.'.format(maiores))