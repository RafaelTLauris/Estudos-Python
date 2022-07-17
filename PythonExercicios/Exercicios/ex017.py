from math import sqrt
des = ' DESAFIO 17 '
print('{:-^60}'.format(des))


print('Vamos descobrir a hipotenusa de um triângulo retângulo!')
catO = float(input('Digite a medida do Cateto Oposto: '))
catA = float(input('Digite a medida do Cateto adjacente: '))
catA = catA ** 2
catO = catO ** 2
som = catO + catA
hip = sqrt(som)
print(catO)
print(catA)
print('A hipotenusa é: {:.2f}'.format(hip))
