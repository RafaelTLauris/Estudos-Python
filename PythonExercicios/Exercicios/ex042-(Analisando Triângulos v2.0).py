'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

r1 = float(input('Digite três valor de reta para vermos se é possível formar um triângulo com eles e se ele'
                 'é um Triângulo Equilátero, Isósceles ou Escaleno:\n '))
r2 = float(input(' '))
r3 = float(input(' '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO')
    if r1 == r2 == r3:
        print('Este triângulo é Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Este triângulo é Escaleno')
    else:
        print('Este triângulo é Isósceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')
