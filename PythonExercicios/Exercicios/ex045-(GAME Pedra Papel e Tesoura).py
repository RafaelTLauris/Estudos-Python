# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

esc = str(input('Escolha entre PEDRA, PAPEL ou TESOURA: '))
pc = ['PEDRA', 'PAPEL', 'TESOURA']
escolhido = choice(pc)
if esc == 'PEDRA' and escolhido == 'PAPEL':
    print('Você escolheu {} e o Computador escolheu {}'.format(esc, escolhido))
    print('VOCÊ PERDEU!')
elif esc == 'PAPEL' and escolhido == 'TESOURA':
    print('Você escolheu {} e o Computador escolheu {}'.format(esc, escolhido))
    print('VOCÊ PERDEU!')
elif esc == 'TESOURA' and escolhido == 'PEDRA':
    print('Você escolheu {} e o Computador escolheu {}'.format(esc, escolhido))
    print('VOCÊ PERDEU!')
elif esc == escolhido:
    print('Você escolheu {} e o Computador escolheu {}'.format(esc, escolhido))
    print('Empatou!')
else:
    print('Você escolheu {} e o Computador escolheu {}'.format(esc, escolhido))
    print('VOCÊ GANHOU!')
