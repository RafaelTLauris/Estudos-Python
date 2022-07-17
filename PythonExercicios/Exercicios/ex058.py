from random import randint

esc = int(input('Escolha um número de 0 à 10: '))
num = randint(0, 10)
tentativa = 0
while esc != num:
    tentativa += 1
    print('O número sorteado foi o {} e você escolheu {}'.format(num, esc))
    esc = int(input('\033[1;31mVocê ERROU\033[m, tente novamente. Escolha um número de 0 à 10: '))
    num = randint(0, 10)
print('\033[1;34mVocê acertou!!! Até você acertar você tentou {} vezes'.format(tentativa))

