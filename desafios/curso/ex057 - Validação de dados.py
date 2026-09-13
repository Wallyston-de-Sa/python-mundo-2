# Desenvolva um programa que leia o sexo de uma pessoa, mas só aceite as respostas "M" ou "F". Caso esteja errado peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo (F) ou (M): ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [F/M]: ')).upper().strip()[0]
print('Sexo {} informado com sucesso!'.format(sexo))

