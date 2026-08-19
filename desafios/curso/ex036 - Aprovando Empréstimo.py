# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então será negado.

# Cores
cor = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
}

# Entrada de dados
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto você ganha mensal? R$'))
ano = int(input('Em quantos anos deseja efetuar o pagamento do imóvel? '))

# Processamento
mensal = ano * 12
prestacao = valor_casa / mensal
permissao = salario * 0.30

# Saída de resultados
print('\nSeu salário é de R${:.2f}. A prestação será de R${:.2f}.'.format(salario, prestacao))
if prestacao <= permissao:
    print('{}Empréstimo Aprovado!{}'.format(cor['verde'], cor['limpa']))
else:
    print('{}Empréstimo negado!{}'.format(cor['vermelho'], cor['limpa']))