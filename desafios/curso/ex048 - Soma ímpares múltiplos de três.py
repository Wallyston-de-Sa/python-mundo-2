# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500
# Contagem
soma = 0
contador = 0

# Entrada de dados e processamento
for cont in range (1, 501, 2):
    if cont % 3 == 0:
        contador += 1
        soma += cont
print('A soma entre todos os {} números ímpares que são multiplos de três entre 1 à 500 é {}'.format(contador, soma))