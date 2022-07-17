from random import randint

num = randint(0, 10)
print('Escolha um número de 0 à 10: ')
acertou = False
tentativa = 0
while not acertou:
    jog = int(input('Qual é seu palpite? '))
    tentativa += 1
    if jog == num:
        acertou = True
    else:
        if jog < num:
            print('Mais... Tente mais uma vez.')
        elif jog > num:
            print('Menos... Tente mais uma vez.')
print('\033[1;34mVocê acertou!!! Até você acertar você tentou {} vezes'.format(tentativa))
