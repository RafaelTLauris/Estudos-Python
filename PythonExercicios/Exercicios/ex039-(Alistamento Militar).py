# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - nasc
if idade < 18:
    print('\033[4;35;40mVocê ainda não precisa se alistar. Faltam {} anos para você se apresentar.'.format(18 - idade))
elif idade > 18:
    print('\033[4;34;40mVocê já passou do tempo de alisamento. Verifique se você está regular!')
else:
    print('\033[4;31;40mEsse ano você deve se apresentar nos postos militares para alistamento!')
