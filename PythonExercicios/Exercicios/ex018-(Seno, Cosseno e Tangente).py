# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
des = ' DESAFIO 18 '
print('{:-^60}'.format(des))


an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))
