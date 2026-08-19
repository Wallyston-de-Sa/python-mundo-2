# Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep

# Entrada de dados
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

print('='*25)
print('Opções: ')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
jogador = int(input('Qual é a sua jogada? '))

# Processamento e saída de resultados
print('JOKEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('='*25)
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('='*25)

if computador == jogador:
    print('EMPATE!')
elif computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 0:
    print('JOGADOR VENCEU!')
elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('COMPUTADOR VENCEU!')
else:
    print('JOGADA INVÁLIDA!')