# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número para descobrir o fatorial dele: '))

while num != 0:
    res = num * num
    num -= 1
print(res)
