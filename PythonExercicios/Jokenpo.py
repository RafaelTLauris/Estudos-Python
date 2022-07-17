from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('{:=^40}'.format(' Jokenpô '))

print('''Suas opções:
    
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

# VALIDADOR DA OPÇÃO DO JOGADOR
while jogador != 0 and jogador != 1 and jogador != 2:
    print('\033[1;31mOpção inválida! Tente novamente\033[m')
    jogador = int(input('Novamente qual seria sua jogada? '))


print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ')
sleep(0.1)
print('-=' * 12)
print('\033[1;33m PC -', 'Jogou {}'.format(itens[pc]))
print('\033[1;34m Você -', 'Jogou {}'.format(itens[jogador]))
print('\033[m-=' * 12)

if pc == 0:
    if jogador == 0:
        print('\033[1;33mEmpatou!')
    elif jogador == 1:
        print('\033[1;36mVOCÊ GANHOU!')
    elif jogador == 2:
        print('\033[1;31mVOCÊ PERDEU!')
    else:
        print('\033[1;31mOpção inválida! Tente novamente')
elif pc == 1:
    if jogador == 0:
        print('\033[1;31mVOCÊ PERDEU!')
    elif jogador == 1:
        print('\033[1;33mEmpatou!')
    elif jogador == 2:
        print('\033[1;36mVOCÊ GANHOU!')
    else:
        print('\033[1;31mOpção inválida! Tente novamente')
elif pc == 2:
    if jogador == 0:
        print('\033[1;36mVOCÊ GANHOU!')
    elif jogador == 1:
        print('\033[1;31mVOCÊ PERDEU!')
    elif jogador == 2:
        print('\033[1;33mEmpatou!')
    else:
        print('\033[1;31mOpção inválida! Tente novamente')

# Print q ficava dentro dos if, elif e else = print('Você escolheu {} e o Computador escolheu {}'.format(jogador, pc))
