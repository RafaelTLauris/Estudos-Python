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
