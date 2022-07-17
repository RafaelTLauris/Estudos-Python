# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual preço do produto? R$'))
novop = p - (p * 5 / 100)
print('O novo preço do produto com desconto de 5% ficou R${:.2f}'.format(novop))
