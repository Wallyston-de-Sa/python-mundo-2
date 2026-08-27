

#Processamento e entrada de dados
for c in range (1, 6):
    nome = str(input('Digite o nome do {}º hóspede: '.format(c)))
    idade = int(input('Digite a sua idade:  '))
    num = int(input('Digite o número do seu quarto: '))

    # Saída de resultados
    print('-'*35)
    print('Hóspede cadastrado com sucesso!')
    print('-'*35)
