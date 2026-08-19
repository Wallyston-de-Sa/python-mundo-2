# Refaça o desafio 035 dos triângulos e acrescente: Equilátero: todos os lados iguais. Isósceles: dois lados iguais. Escaleno: todos os lados diferentes.

# Entrada de dados
lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo lado: '))
lado3 = float(input('Terceiro lado: '))

# Processamento e saída de resultados
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado3:
    print('Os segmentos se tornaram um triângulo.')
    if lado1 == lado2 == lado3:
        print('É um triângulo EQUILÁTERO')
    elif lado1 != lado2 != lado3:
        print('É um triângulo ESCALENO')
    else:
        print('É um triângulo ISÓSCELES')
else:
    print('Os segmentos não se tornam um triângulo!')