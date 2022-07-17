nome = str(input('Qual seu nome?'))

if nome == 'Rafael':
    print('Que nome perfeito o seu!')
elif nome == 'Ademilde' or nome == 'Marcio' or nome == 'Renata':
    print('Seu nome está presente dentro da minha família sabeia?!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))
