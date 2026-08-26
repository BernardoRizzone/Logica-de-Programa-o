ct = 0
soma =0
print('Digite -1 para sair')
while True:
    numero = int(input('\nDigite um valor: '))
    if numero == -1:
        break
    ct = ct + 1
    soma = soma + numero
print('O numero de numeros colocados foi:', ct)
print('A soma dos numero é:', soma)
