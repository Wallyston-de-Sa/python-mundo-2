#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior. O segundo valor é maior. Não existe valor maior, os dois são iguais

# Entrada de dados
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

#Processamento e saída de dados
print('='*20)
print('     COMPARANDO')
print('='*20)
if num1 < num2:
    print('O valor {} é maior que {}'.format(num2, num1))
elif num1 > num2:
    print('O valor {} é maior que {}'.format(num1, num2))
else:
    print('Não existe valor maior, os dois são iguais {}'.format(num1))