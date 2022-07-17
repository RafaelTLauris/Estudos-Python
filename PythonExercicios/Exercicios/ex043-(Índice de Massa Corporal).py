'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

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
