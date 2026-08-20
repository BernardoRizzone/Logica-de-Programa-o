numero = int(input("Digite um numero inteiro:"))
print('\nnumero digitado:', numero)

resto = numero %2

if numero % 2 == 0:
    print('O numero é Par')
    print('O resto é:', resto)
else:
    print('O numero é impar!')
    print('O resto é:', resto)