import random
num = random.randint(0, 5)
esc = int(input('Escolha um número de 0 à 5: '))
if esc == num:
    print('Você acertou!!!')
else:
    print('Você perdeu...')
print('O número sorteado foi o {}'.format(num))
