km = float(input('Digite em Km a distância da viagem que irá fazer: '))

'''if km <= 200:
    preco = km * 0.50
    print('O valor da viagem no total ficará de R${:.2f} - Viagem Curta'.format(preco))
elif km > 200:
    preco = km * 0.45
    print('O valor da viagem no total ficará de R${:.2f} - Viagem Longa.'.format(preco))'''

preco = km * 0.50 if km <= 200 else km * 0.45
print('O valor da viagem no total ficará de R${:.2f}'.format(preco))
