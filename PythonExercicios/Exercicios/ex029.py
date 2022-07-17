vel = float(input('Velocidade atual do carro: '))
if vel > 80:
    print('Perdeu Playboy, você foi multado!')
    multa = (vel - 80) * 7
    print('O valor da multa ficou R${:.2f}'.format(multa))
else:
    print('Ta tranquilo Playboy você está dentro dos limites de velocidade da via')
