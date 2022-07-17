from math import hypot
des = ' Outra forma '
print('{:-^60}'.format(des))


print('Vamos descobrir a hipotenusa de um triângulo retângulo!')
catO = float(input('Digite a medida do Cateto Oposto: '))
catA = float(input('Digite a medida do Cateto adjacente: '))
hip = hypot(catO, catA)
print('A hipotenusa é: {:.2f}'.format(hip))
