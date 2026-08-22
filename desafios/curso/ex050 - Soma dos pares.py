# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

# Entrada de dados
soma = 0
for num in range(1, 7):
    int(input('Digite {}ª número: '.format(num)))
    if num % 2 == 0: 
        soma += num

# Saida de resultados
print('A soma total de todos os números pares é {}'.format(soma))