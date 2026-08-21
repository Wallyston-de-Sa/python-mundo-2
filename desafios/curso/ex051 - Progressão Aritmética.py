# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Entrada de dados
cont = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))


#Saída de resultados
print('Os 10 primeiros termos dessa progressão é:')
for c in range(10):
     print(cont + c * razao, end=' → ')
print('ACABOU!!')
