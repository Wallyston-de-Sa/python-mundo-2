# Crie um programa que leia uma frase qualquer e diga se ela é políndromo, desconsiderando os espaços

# Entrada de dados
frase = str(input('Digite uma frase: ')).upper().strip()

# Manipulando String
separando = frase.split()
junto = ''.join(separando)
inverso = junto[::-1]

# Saída de resultado
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um POLÍNDROMO.')
else:
    print('A frase NÃO é um POLINDROMO')