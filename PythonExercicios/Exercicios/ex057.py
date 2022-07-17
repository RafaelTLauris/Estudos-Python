sexo = str(input('Digite seu Sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    print('\033[1:31mDigite uma opção de sexo válida!\033[m')
    sexo = str(input('Digite seu Sexo [M/F]: ')).upper().strip()
print('\033[4;36mSexo ({}) validado com sucesso!'.format(sexo))
