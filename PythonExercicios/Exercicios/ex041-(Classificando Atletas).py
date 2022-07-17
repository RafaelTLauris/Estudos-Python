''' Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date

nome = str(input('Digite seu nome: '))
nasc = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - nasc

if idade <= 9:
    print('A categoria do(a) atleta {} é a MIRIM, pois ele tem {} anos.'.format(nome, idade))
elif idade <= 14:
    print('A categoria do(a) atleta {} é a INFANTIL, pois ele tem {} anos.'.format(nome, idade))
elif idade <= 19:
    print('A categoria do(a) atleta {} é a JUNIOR, pois ele tem {} anos.'.format(nome, idade))
elif idade <= 25:
    print('A categoria do(a) atleta {} é a SÊNIOR, pois ele tem {} anos.'.format(nome, idade))
else:
    print('A categoria do(a) atleta {} é a MASTER, pois ele tem {} anos.'.format(nome, idade))
