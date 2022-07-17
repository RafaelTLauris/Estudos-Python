print('==========Desafio 5==========')

n = int(input('Digite um número: '))
su = n + 1
an = n - 1
print('O sucessor do número {} é: {}\nE seu antecessor é: {}'.format(n, su, an))

print('                             ')
print('==========Desafio 6==========')

n = int(input('Digite um número: '))
do = n * 2
tr = n * 3
ra = n ** (1/2)
print('O dobro do número escolhido é: {}\nseu triplo é: {}\ne sua raiz é: {:.2f}'.format(do, tr, ra))

print('                             ')
print('==========Desafio 7==========')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = nota1 + nota2
print('a média do aluno é: {}'.format(media/2))

print('                             ')
print('==========Desafio 8==========')

v = float(input('Digite um valor em metros: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
cm = v * 100
mm = v * 1000
print('O valor digitado em Quilômetros é: {}km'
      '\n em Hectômetros é: {}hm'
      '\n em Decâmetros é: {}dam'
      '\n em Decímetros é: {:.0f}dm\n em centimetros é: {:.0f}cm'
      '\n e em milímetros é: {:.0f}mm'.format(km, hm, dam, dm, cm, mm))

print('                             ')
print('==========Desafio 9==========')

n = int(input('Digite um número que deseja saber a tabuada: '))

print('{} X 1 = {}'.format(n, n*1))
print('{} X 2 = {}'.format(n, n*2))
print('{} X 3 = {}'.format(n, n*3))
print('{} X 4 = {}'.format(n, n*4))
print('{} X 5 = {}'.format(n, n*5))
print('{} X 6 = {}'.format(n, n*6))
print('{} X 7 = {}'.format(n, n*7))
print('{} X 8 = {}'.format(n, n*8))
print('{} X 9 = {}'.format(n, n*9))
print('{} X 10 = {}'.format(n, n*10))

print('                             ')
print('==========Desafio 10==========')

din = float(input('Digite quantos reais você tem na carteira? R$'))
dol = din / 4.98

print('Seu dinheiro, R${} convertendo em dólares ficaria: U${:.2f}'.format(din, dol))

print('                             ')
print('==========Desafio 11==========')

alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
ar = alt * larg
lit = ar / 2
print('Serão necessários {} litros de tinta para pintar a área total da parede que é de {} m²'.format(lit, ar))

print('                             ')
print('==========Desafio 12==========')

pre = float(input('Digite o valor do produto? R$ '))
prom = pre * 0.05
print('Esse produto na promoção vai sair por R${:.2f}'.format(pre - prom))

print('                             ')
print('==========Desafio 13==========')

sala = float(input('Digite seu salário: '))
alm = sala * 0.15
print('Seu salário com aumento de 15% ficou R${:.2f}'.format(sala + alm))