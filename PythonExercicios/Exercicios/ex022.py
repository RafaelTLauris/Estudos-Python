nome = str(input('Digite seu nome completo: ')).strip()  # .strip() elimina os espaços antes e depois
print(nome.upper())
print(nome.lower())
print(format(len(nome) - nome.count(' ')))
print(nome.find(' '))
