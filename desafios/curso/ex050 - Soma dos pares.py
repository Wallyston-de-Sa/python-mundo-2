# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

# Contadores
soma = 0
cont = 0

# Entrada de dados e processamento
for num in range(1, 7):
    int(input('Digite {}ª número: '.format(num)))
    # Verificação
    if num % 2 == 0: 
        soma += num
        cont += 1

# Saida de resultados
print('A soma total de todos os {} números pares é {}'.format(cont, soma))