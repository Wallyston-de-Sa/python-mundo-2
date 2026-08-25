# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo. Qual é o nome do homem mais velho. Quantas mulheres tem menos de 20 anos.

# Entrada de dados
homemvelho = ''
idadehomem = 0
somaidade = 0
mulhernova = 0

# Entrada de dados e Processamento
for c in range (1, 5):
    nome = str(input('Digite o nome da {}º pessoa: '.format(c))).strip().title()
    idade = int(input('Digite sua idade: '))
    genero = str(input('Qual é o seu gênero? (M) Masculino. (F) Feminino: ')).upper().strip()

    # Mulheres com menos de 20 anos.
    if genero == 'F' and idade < 20:
        mulhernova += 1

    # Soma a idade para calcular a média
    somaidade += idade

    # Manipulação para identificar o homem mais velho
    if genero == 'M':
        if c == 1:
            homemvelho = nome
            idadehomem = idade
        elif idade > idadehomem:
            homemvelho = nome
            idadehomem = idade

# Média de idade do grupo
media = somaidade / 4

# Saída de resultados
print('-'*35)
print('A média de idade do grupo é {} anos'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(homemvelho, idadehomem))
print('No grupo tem {} mulheres com menos de 20 anos.'.format(mulhernova))
print('-'*35)

