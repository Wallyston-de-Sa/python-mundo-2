# Crie um programa que leia dois valores e mostre um menu como ao lado na tela: 1 - Somas, 2- Multiplicar, 3- maior, 4 - novos números, 5 - sair do programa.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 0

while opc != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opc = int(input('Digite sua opção: '))
    if opc == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1+n2))
    elif opc == 2:
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, n1*n2))
    elif opc == 3:
        if n1 > n2:
            maior = n1
        elif n1 < n2:
            maior = n2
        print('Entre {} e {} o maior número é {}'.format(n1, n2, maior))
    elif opc == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')