s = 0
c = 0
for a in range(1, 7):
    n = int(input('Digite o {} número: '.format(a)))
    if n % 2 == 0:
        s += n
        c += 1
print('Você informou {} números PARES e a soma foi {}'.format(c, s))
