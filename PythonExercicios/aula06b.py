v = input('Digite algum coisa: ')
print('Sua forma primitiva é?', type(v))
print('É um número?', v.isnumeric())
print('É alfabético?', v.isalpha())
print('É um alfanumérico?', v.isalnum())
print('Está em maiusculas?', v.isupper())
print('Está em maiusculas?', v.islower())
print('Só tem espaços?', v.isspace())
print('Ela está capitalizada?', v.istitle())