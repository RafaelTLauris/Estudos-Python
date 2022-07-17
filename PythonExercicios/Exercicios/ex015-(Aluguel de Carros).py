# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input('Por quantos dias você alugou o carro: '))
km = float(input('Quantos Km foram rodados: '))
pago = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
