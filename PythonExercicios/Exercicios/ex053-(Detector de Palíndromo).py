# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()  # split() método q divide uma string em uma lista.
junto = ''.join(palavras)
# inverso = ''

inverso = junto[::-1]

# for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um Palíndromo!')
else:
    print('A frase não é um palímdromo!')
