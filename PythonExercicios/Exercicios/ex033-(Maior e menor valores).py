# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite um terceiro número: '))

#verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O número {} é o menor '.format(menor))
print('O número {} é o maior '.format(maior))


# OU


if n1 > n2 > n3:
    print('O número {} é o maior '.format(n1))
    print('O número {} é o menor '.format(n3))
elif n1 > n3 > n2:
    print('O número {} é o maior '.format(n1))
    print('O número {} é o menor '.format(n2))
elif n2 > n3 > n1:
    print('O número {} é o maior '.format(n2))
    print('O número {} é o menor '.format(n1))
elif n2 > n1 > n3:
    print('O número {} é o maior '.format(n2))
    print('O número {} é o menor '.format(n3))
elif n3 > n2 > n1:
    print('O número {} é o maior '.format(n3))
    print('O número {} é o menor '.format(n1))
elif n3 > n1 > n2:
    print('O número {} é o maior '.format(n3))
    print('O número {} é o menor '.format(n2))