from datetime import date

nasc = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - nasc
if idade < 18:
    print('\033[4;35;40mVocê ainda não precisa se alistar. Faltam {} anos para você se apresentar.'.format(18 - idade))
elif idade > 18:
    print('\033[4;34;40mVocê já passou do tempo de alisamento. Verifique se você está regular!')
else:
    print('\033[4;31;40mEsse ano você deve se apresentar nos postos militares para alistamento!')
