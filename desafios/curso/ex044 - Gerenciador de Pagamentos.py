# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: À vista dinheiro/cheque: 10% de desconto. À vista no cartão: 5% de desconto. Em até 2x no cartão: preço normal. 3x ou mais no cartão: 20% de juros

# Entrada de dados
produto = float(input('Digite o valor do produto: R$'))

print('-'*40)
print('FORMA DE PAGAMENTO: ')
print('[1] para À VISTA DINHEIRO OU CHEQUE')
print('[2] para À VISTA NO CARTÃO')
print('[3] para EM ATÉ 2x NO CARTÃO DE CRÉDITO')
print('[4] para 3x ou mais no CARTÃO DE CRÉDITO')
opc = int(input('>>> OPÇÃO: '))
print('-'*40)

# Processamento e saída de resultados
if opc == 1:
    desc = produto - (produto * 10/100)
    print('Foi inserido a opção "A VISTA DINHEIRO OU CHEQUE"')
    print('O produto custa R${:.2f}.'.format(produto))
    print('Vamos fornecer um desconto de 10% para a sua compra!')
    print('O valor final será de R${:.2f}'.format(desc))
elif opc == 2:
    desc = produto - (produto * 5/100)
    print('Foi inserido a opção "A VISTA NO CARTÃO"')
    print('O produto custa R${:.2f}.'.format(produto))
    print('Vamos fornecer um desconto de 5% para a sua compra!')
    print('O valor final será de R${:.2f}'.format(desc))
elif opc == 3:
    print('Foi inserido a opção "EM ATÉ 2X NO CARTÃO"')
    print('O produto custa R${:.2f}'.format(produto))
    print('Não conseguimos fornecer nenhum desconto com essa opção!')
    print('O valor final será de R${:.2f}'.format(produto))
elif opc == 4:
    juros = produto + (produto * 20/100)
    print('Foi inserido a opção "3x OU MAIS NO CARTÃO DE CRÉDITO"')
    print('O produto custa R${:.2f}.'.format(produto))
    print('Vamos solicitar um juros de 20% para a sua compra!')
    print('O valor final será de R${:.2f}'.format(juros))