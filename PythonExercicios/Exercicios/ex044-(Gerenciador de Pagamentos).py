'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJAS LAURITZ '))
valor = float(input('Digite o valor do produto:\nR$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    print('O valor total do pagamento ficou de R${:.2f}'.format(valor - (valor * 0.1)))
elif opção == 2:
    print('O valor total do pagamento ficou de R${:.2f}'.format(valor - (valor * 0.05)))
elif opção == 3:
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    print('O valor total do pagamento ficou de R${:.2f}'.format(valor))
elif opção == 4:
    totalP = int(input('Quantas parcelas? '))
    valor = valor + (valor * 0.2)
    parcela = valor / totalP
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalP, parcela))
    print('O valor toral do pagamento ficou de R${:.2f}'.format(valor))
else:
    valor = valor
    print('\033[2;31mOpção inválida de pagamento. Tente novamente!')
