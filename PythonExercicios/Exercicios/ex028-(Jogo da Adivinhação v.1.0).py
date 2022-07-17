# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
num = randint(0, 5)
esc = int(input('Escolha um número de 0 à 5: '))
if esc == num:
    print('Você acertou!!!')
else:
    print('Você perdeu...')
print('O número sorteado foi o {}'.format(num))
