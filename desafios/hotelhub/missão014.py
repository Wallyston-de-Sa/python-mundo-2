# Entrada de dados e processamento
for c in range (10):
    print('-'*35)
    quarto = int(input('Número do quarto: '))
    situacao = input('Situação do quarto: (L), (O), (M) ').upper().strip()
# Verificação e saída de resultados
    if situacao == 'L':
        print('Quarto {} - Livre'.format(quarto))
    elif situacao == 'O':
        print('Quarto {} - Ocupado'.format(quarto))
    elif situacao == 'M':
        print('Quarto {} - Manutenção'.format(quarto))
    else:
        print('Informação Inválida!')