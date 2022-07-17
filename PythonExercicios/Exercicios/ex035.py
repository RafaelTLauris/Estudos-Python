r1 = float(input('Digite três valor de reta para vermos se é possível formar um triângulo com eles:\n '))
r2 = float(input(' '))
r3 = float(input(' '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIÂNGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO')


#   FORMULA
#    | b - c | < a < b + c
#    | a - c | < b < a + c
#    | a - b | < c < a + b

