# CALCULADORA

import math

print('Calculadora do Rafa!')
n1 = float(input('Digite um número: '))
print('Escolha um desses operadores:')
print(' +  -  X  / ')
ope = str(input(''))
n2 = float(input('Digite outro número: '))

if ope == '+':
    res = n1 + n2
    print('Resultado: {}'.format(res))
elif ope == '-':
    res = n1 - n2
    print('Resultado: {}'.format(res))
elif ope == 'X':
    res = n1 * n2
    print('Resultado: {}'.format(res))
elif ope == '/':
    res = n1 / n2
    print('Resultado: {}'.format(res))
