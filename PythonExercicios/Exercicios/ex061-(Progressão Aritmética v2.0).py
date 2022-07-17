# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

t1 = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = t1
cont = 1

while cont <= 10:
    print('{} ⇀ '.format(termo), end='')
    termo += razão
    cont += 1
print('Fim')
