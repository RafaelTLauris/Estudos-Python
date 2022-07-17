# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do seu salário: R$'))
novo = salario + (salario * 15 / 100)
print('Seu salário antigo era de R${:.2f}. Agora seu salário com o reajuste de aumento ficou R${:.2f}'.format(salario, novo))
