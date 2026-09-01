# Entrada de dados
dias = int(input('Quantos dias tem sua hospedagem? '))

# Verificação e saída de resultados
if dias <= 2:
    print('Hospedagem curta')
elif dias <= 7:
    print('Hospedagem média')
else:
    print('Hospedagem longa')