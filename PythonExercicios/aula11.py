nome = 'Rafael T Lauris'
cores = { 'limpa':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
print('\033[1;35;40mTenho 20 anos!')


# CÓDIGO PARA MUDAR DE CORES

#   \033[_;__;__m
#   Style = 0, 1, 4, 7
#   Text = 30, 31, 32, 33, 34, 35, 36, 37
#   Back = 40, 41, 42, 43, 44, 45, 46, 47
