media = 0
somaidade = 0
maiorh = 0
nomevelho = ''
totmulher20 = 0
for a in range(1, 5):
    print('{:=^30}'.format('Dados da {}° pessoa'.format(a)))
    nome = str(input('Qual seu nome? ')).strip()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? [M/F] ')).strip()
    somaidade += idade
    if a == 1 and sexo in 'Mm':
        maiorh = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maiorh:
        maiorh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = somaidade / 4
print('A média de idade das 4 pessoas é de {:.2f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorh, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
