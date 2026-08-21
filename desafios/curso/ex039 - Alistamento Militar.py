#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - Se já passou do tempo do alistamento. O programa deverá mostrar o tempo que falta ou o tempo que passou.
from datetime import date

# Entrada de dados
nascimento = int(input('Digite o ano em que você nasceu: '))

# Processamento
ano = date.today().year
idade = ano - nascimento
diferenca_novo = nascimento + 18
diferenca_velho = nascimento + 18

# Saída de resultados
print('\nVocê está com {} anos.'.format(idade))
if idade == 18:
    print('Você deve se alistar nesse ano!')
elif idade < 18:
    saldo = 18 - idade
    print('Você não precisa se alistar agora. O ano do seu alistamento será em {}, faltam {} anos.'.format(diferenca_novo, saldo))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado em {}, {} anos atrás.'.format(diferenca_velho, saldo))