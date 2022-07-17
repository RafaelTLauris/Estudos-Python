nome = str(input('Qual o nome do aluno: '))
nota1 = float(input('Primeira nota:\n'))
nota2 = float(input('Segunda nota:\n'))
media = (nota1 + nota2) / 2

if media <= 5.0:
    print('\033[1;31mO aluno(a) {} foi Reprovado pois sua média é {:.1f} :('.format(nome, media))
elif media <= 6.9:
    print('\033[1;33mO aluno(a) {} está de recuperação pois sua média é {:.1f}  :/'.format(nome, media))
elif media >= 7:
    print('\033[1;32mO aluno(a) {} foi aprovado pois sua média é {:.1f}  :D'.format(nome, media))
