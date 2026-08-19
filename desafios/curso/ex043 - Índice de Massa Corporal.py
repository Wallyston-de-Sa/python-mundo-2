# Desenvolva uma lógica que leia o peso e altura de uma pessoa e calcule seu IMC. Abaixo de 18.5: Abaixo do peso. 18.5 e 25: Peso ideal. 25 até 30: Sobrepeso. 30 até 40: Obesidade. Acima de 40: Obesidade mórbida. 

# Entrada de dados
kg = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura: '))

# Processamento
imc = kg / (altura * altura)

# Saída de resultados
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('CUIDADO!')
    print('Você está com obesidade mórbida')