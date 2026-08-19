# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: Mirim. Até 14: Infantil. Até 19 anos: Junior. Até 20 anos: Sênior. Acima: MASTER.
from datetime import date

# Entrada de dados
nascimento = int(input('Digite o seu ano de nascimento: '))

# Processamento
idade = date.today().year - nascimento

# Saída de resultados
print('='*25)
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você participará da categoria: MIRIM')
elif idade <= 14:
    print('Você participará da categoria: INFANTIL')
elif idade <= 19:
    print('Você participará da categoria: JUNIOR')
elif idade <= 20:
    print('Você participará da categoria: SÊNIOR')
else:
    print('Você participará da categoria: MASTER')