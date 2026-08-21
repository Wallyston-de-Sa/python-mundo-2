# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

# Entrada de dados
num = int(input('Digite um número para a tabuada: '))
for n in range(0, 11):
    print('{} x {} = {}'.format(num, n, n * num))