# Contadores
menor = 0
adulto = 0
idoso = 0

# Entrada de dados e processamento
for c in range (1, 6):
    print('='*35)
    nome = input('Nome do {}º hóspede: '.format(c)).strip().title()
    idade = int(input('Idade: '))
    if idade < 18:
        menor += 1
    elif idade <= 59:
        adulto += 1
    else:
        idoso += 1

# Saída de resultados
print('='*35)
print('No grupo tem {} menor de idade.'.format(menor))
print('{} Adulto.'.format(adulto))
print('{} Idoso'.format(idoso))