dia = int(input('Por quantos dias você alugou o carro: '))
km = float(input('Quantos Km foram rodados: '))
pago = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
