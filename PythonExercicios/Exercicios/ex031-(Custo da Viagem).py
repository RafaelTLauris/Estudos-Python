# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Digite em Km a distância da viagem que irá fazer: '))

if km <= 200:
    preco = km * 0.50
    print('O valor da viagem no total ficará de R${:.2f} - Viagem Curta'.format(preco))
elif km > 200:
    preco = km * 0.45
    print('O valor da viagem no total ficará de R${:.2f} - Viagem Longa.'.format(preco))


# OU


preco = km * 0.50 if km <= 200 else km * 0.45
print('O valor da viagem no total ficará de R${:.2f}'.format(preco))
