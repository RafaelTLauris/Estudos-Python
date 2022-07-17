salario = float(input('Informe seu sálario para calcularmos seu aumento: R$'))

if salario >= 1250:
    aumento = salario + (salario * 0.10)
    print('Seu salário com o aumento ficou R${}'.format(aumento))
elif salario < 1250:
    aumento = salario + (salario * 0.15)
    print('Seu salário com o aumento ficou R${}{}'.format('\033[1;35m', aumento))
