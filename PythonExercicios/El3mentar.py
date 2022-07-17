# Jogo de escolhas de uma História Fictícia

print('{:=^30}'.format(' El3mentar CAP I '))
print(' ')
opcao = 0
while opcao != 4:
    print('{:-^40}!'.format(' MENU '))
    print('Bem Vindo ao CAP I de El3mentar!')
    print('''
    [ 1 ] NOVO JOGAR
    [ 2 ] CARREGAR
    [ 3 ] CRÉDITOS
    [ 4 ] SAIR
    ''')
    opcao = int(input('Escolha a sua opção '))
    if opcao == 1:
        print('')

    elif opcao == 2:
        print('')

    elif opcao == 3:
        print('{:-^40}!'.format(' CRÉDITOS '))
        print('História e Jogo criados por Rafael T. Lauris.')

    elif opcao == 4:
        print('Finalizando...')

print('Fechando Jogo...')

