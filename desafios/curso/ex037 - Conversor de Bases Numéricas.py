# Escreva um programa que leia um número inteiro qualquer e pela para o usuário escolher qual será a base de conversão: 1- Binário. 2- Octal. 3- Hexadecimal.

# Entrada de dados
num = int(input('Digite um número qualquer: '))

print('ESCOLHA EM QUAL BASE VOCê QUER SUA CONVERSÃO: ')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
opcao = int(input('>>> Opção: '))

# Processamento e saída de resultados
if opcao == 1:
    print('O número {} na base binária se torna {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} na base Octal se torna {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} na base Hexadecimal se torna {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')