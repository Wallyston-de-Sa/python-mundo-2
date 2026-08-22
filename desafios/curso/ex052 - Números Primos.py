# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

# Entrada de dados
num = int(input('Qual número deseja saber se é primo? '))

# Contador
cont = 0

for c in range(1, num + 1):
    if num %  c == 0:
        cont += 1
    print(c, end=' ')

# Saída de resultados
print('\nO número {} foi divisível {}º vezes.'.format(num, cont))
if cont == 2:
    print('Ele é um número PRIMO!')
else:
    print('Ele NÃO é um número PRIMO!')

