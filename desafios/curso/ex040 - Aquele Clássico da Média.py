# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO. - Média entre 5., e 6.9: RECUPERAÇÃO. - Média 7.0 ou superior: APROVADO.
# Cores
# Cores
cor = {
    'limpa': '\033[m',
    'Amarelo': '\033[33m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
}

# Entrada de dados
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

# Processamento
media = (nota1 + nota2) / 2

# Saída de resultados
print('-'*30)
print('Sua média é {}'.format(media))
if media < 5.0:
    print('{}Você está reprovado!{}'.format(cor['vermelho'], cor['limpa']))
elif media <= 6.9:
    print('{}Você está em recuperação!{}'.format(cor['Amarelo'], cor['limpa']))
else:
    print('{}Você está aprovado!{}'.format(cor['verde'], cor['limpa']))
