vcasa = float(input('Qual é o valor da casa que deseja comprar?\nR$'))
salario = float(input('Qual é seu salário?\nR$'))
qanos = int(input('E em quantos anos pretende pagar essa casa?\n'))

meds = vcasa / (qanos * 12)
minimo = salario * 30 / 100

if meds <= minimo:
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(vcasa, qanos))
    print('A prestação será de R${:.2f}'.format(meds))

    print('Você poderá comprar sua casa!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos'.format(vcasa, qanos))
    print('A prestação será de R${:.2f}'.format(meds))

    print('Infelizmente você não poderá comprar essa casa!')
