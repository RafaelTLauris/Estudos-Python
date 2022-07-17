s = 0
c = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        c += 1
        s += a
print('A soma de todos os {} valores é {}'.format(c, a))
