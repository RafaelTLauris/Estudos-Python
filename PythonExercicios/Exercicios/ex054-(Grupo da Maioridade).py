# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

totmaior = 0
totmenor = 0

for a in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(a)))
    idade = date.today().year - nasc
    if idade < 59:
        totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoas idosas'.format(totmaior))
print('Ao todo tivemos {} pessoas jovens'.format(totmenor))
