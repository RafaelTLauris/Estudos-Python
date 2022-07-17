# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

t1 = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = t1 + (10 - 1) * razão

while :
    print('{}'.format(décimo))
