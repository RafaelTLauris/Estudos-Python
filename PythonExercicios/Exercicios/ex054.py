from datetime import date

totmaior = 0
totmenor = 0

for a in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(a)))
    idade = date.today().year - nasc
    if idade < 59:
        totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoas idosas'.format(totmaior))
print('Ao todo tivemos {} pessoas jovens'.format(totmenor))
