from math import trunc
des = ' DESAFIO 19 '
print('{:-^60}'.format(des))


num = float(input('Digite um número real para descobrir sua porção interia: '))
print('A porção inteira do número: {} é {}'.format(num, trunc(num)))
