# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500
# Entrada de dados
soma = 0

# Saída de resultados
for cont in range (1, 501):
    if cont % 2 != 0 and cont % 3 == 0:
        soma += cont
print('A soma entre todos os números ímpares que são multiplos de três entre 1 à 500 é {}'.format(soma))