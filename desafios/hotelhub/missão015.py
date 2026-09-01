# Entrada de dados e processamento
for c in range(5):
    print('='*35)
    nome = input('Nome do hóspede: ').title().strip()
    quarto = int(input('Número do quarto: '))
    dias = int(input('Quantidade de dias da hospedagem: '))
    situacao = input('"S" para Disponível. "N" para indisponível: ').upper().strip()

# Verificação e saída de resultados
    if situacao == 'S':
        print('-'*35)
        print('Reserva liberada!')
        print('Hóspede: {}'.format(nome))
        print('Quarto: {}'.format(quarto))
        print('Hospedagem: {} dias'.format(dias))
    elif situacao == 'N':
        print('-'*35)
        print('Reserva não realizada!')
        print('Quarto indisponível.')
    else:
        print('Informação inválida! Tente novamente.')

