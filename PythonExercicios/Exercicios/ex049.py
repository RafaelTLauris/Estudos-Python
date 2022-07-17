num = int(input('Digite um número que deseja saber a tabuada: '))
b = 0
for a in range(1, 11):
    b += 1
    print('{} X {} = {}'.format(num, b, num * b))
