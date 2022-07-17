# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe seu sálario para calcularmos seu aumento: R$'))

if salario >= 1250:
    aumento = salario + (salario * 0.10)
    print('Seu salário com o aumento ficou R${}'.format(aumento))
elif salario < 1250:
    aumento = salario + (salario * 0.15)
    print('Seu salário com o aumento ficou R${}{}'.format('\033[1;35m', aumento))
