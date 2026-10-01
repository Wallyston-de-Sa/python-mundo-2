# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
pensar = randint(0, 10)
print('Pensei em um número entre 1 à 10. Será que você consegue acertar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == pensar:
        acertou = True
    else:
        if jogador > pensar:
            print('Menos... Tente novamente')
        if jogador < pensar:
            print('Mais... Tente novamente')
print('Acertou!')
print('Você acertou na {}º tentativa. '.format(palpite))