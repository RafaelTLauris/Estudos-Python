t1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = t1 + (10 - 1) * razão

print(décimo)
for c in range(t1, décimo, razão):
    print('{}'.format(c))
