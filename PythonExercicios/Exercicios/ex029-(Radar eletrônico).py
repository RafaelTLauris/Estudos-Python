# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Velocidade atual do carro: '))
if vel > 80:
    print('Perdeu Playboy, você foi multado!')
    multa = (vel - 80) * 7
    print('O valor da multa ficou R${:.2f}'.format(multa))
else:
    print('Ta tranquilo Playboy você está dentro dos limites de velocidade da via')
