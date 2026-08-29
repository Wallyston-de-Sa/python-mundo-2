# Cores na interface
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
}

# Entrada de dados e processamento
for c in range(1, 4):
    print('='*45)
    hospede = str(input('Nome do hóspede: ')).strip().title()
    numero = int(input('Número do quarto: '))
    situacao = str(input('Situação do quarto "S" ou "N": ')).upper().strip()

# Verificação e saída de resultados
    if situacao == 'S':
        print('{}Reserva liberada{}'.format(cores['verde'], cores['limpa']))
        print('Hóspede: {}'.format(hospede))
        print('Quarto: {}'.format(numero))
    else:
        print('{}Reserva não realizada{}'.format(cores['vermelho'], cores['limpa']))
        print('Quarto: {} indisponível.'.format(numero))
    