for a in range(0, 5):
    print('Oi')
print('Fim')
# -------------------------------------------------------------------------------------------------------------
for b in range(5, 0, -1):
    print(b)
print('Fim')
# -------------------------------------------------------------------------------------------------------------
for c in range (0, 7, 2):
    print(c)
print('Fim')
# -------------------------------------------------------------------------------------------------------------
n = int(input('Digite um número: '))
for d in range(0, n+1):
    print(d)
print('Fim')
# -------------------------------------------------------------------------------------------------------------
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for e in range(i, f+1, p):
    print(e)
print('Fim')
# -------------------------------------------------------------------------------------------------------------
s = 0
for f in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
