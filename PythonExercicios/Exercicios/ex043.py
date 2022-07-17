peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Peso ideal')
elif 25 <= imc < 30:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Obesidade')
else:
    print('Obesidade Mórbida, CUIDADO!')
