# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

# Entrada de dados
maior = 0
menor = 0

# Entrada de dados e processamento
for p in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa (Kg): '.format(p)))

    # Manipulação para o maior e menor peso
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

# Saída de resultados
print('O maior peso é o {}'.format(maior))
print('O menor peso é o {}'.format(menor))
