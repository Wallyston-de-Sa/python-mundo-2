# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

# Cores
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m' }

# Contador
cont = 0

# Entrada de dados e processamento
num = int(input('Qual número deseja saber se é primo? '))
for c in range(1, num + 1):
    if num %  c == 0:
        print('{}{}{}'.format(cores['verde'], c, cores['limpa']), end=' ')
        cont += 1
    else:
        print('{}{}{}'.format(cores['vermelho'], c, cores['limpa']), end=' ')


# Saída de resultados
print('\nO número {} foi divisível {}º vezes.'.format(num, cont))
if cont == 2:
    print('Ele é um número PRIMO!')
else:
    print('Ele NÃO é um número PRIMO!')

