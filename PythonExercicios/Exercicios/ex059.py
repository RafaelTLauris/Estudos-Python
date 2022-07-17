num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
print('''O que vc deseja fazer com os valores escolhidos?
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
opção = int(input('Escolha uma opção: '))
while opção != 1 != 2 != 3 != 4 != 5:
    print('Opção inválida')
    print('''O que vc deseja fazer com os valores escolhidos?
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Escolha uma opção: '))
if opção == 1:
    res = 0
    res = num1 + num2
    print('A soma dos valores é {}'.format(res))
elif opção == 2:
    res = 0
    res = num1 * num2
    print('A soma dos valores é {}'.format(res))
elif opção == 3:
    if num1 > num2:
        print('O número {} é maior que o número {}'.format(num1, num2))
    else:
        print('O número {} é maior que o número {}'.format(num2, num1))
