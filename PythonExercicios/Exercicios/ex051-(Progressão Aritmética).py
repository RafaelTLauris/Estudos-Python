# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

t1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = t1 + (10 - 1) * razão

print(décimo)
for c in range(t1, décimo, razão):
    print('{}'.format(c))
