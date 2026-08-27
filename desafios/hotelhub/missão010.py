

# Entrada de dados e processamento
for c in range(1, 6):
    print('QUARTO {}'.format(c))
    quarto = int(input('\nDigite o número do quarto: '))
    situacao = str(input('"L" Liberado ou "O" Ocupado: ')).upper().strip()

# Verificação e saída de resultados
    if situacao == 'L':
        print('='*25)
        print('Quarto {} está liberado!'.format(quarto))
        print('='*25)
    else:
        print('='*25)
        print('Quarto {} está ocupado!'.format(quarto))
        print('='*25)