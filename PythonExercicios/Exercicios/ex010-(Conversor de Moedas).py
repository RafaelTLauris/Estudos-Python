# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Quanto dinheiro em você tem na carteira? R$'))
dolar = dinheiro / 5.41
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(dinheiro, dolar))
