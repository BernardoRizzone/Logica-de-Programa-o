menor_valor = 99999999
maior_valor = -9999999
ct = 0
soma = 0

print("Digite o [0] para sair:")
while True:
    valor = int(input('\nDigite um valor: '))
    if valor == 0:
        break

    if menor_valor > valor:
        menor_valor = valor

    if valor > maior_valor:
        maior_valor = valor

    ct += 1
    soma = soma +valor
media = soma/ct
print('\nO menor valor é:', menor_valor)
print('O maior valor é:', maior_valor)
print('A quantidade de valores digitados foi:', ct)
print('A soma dos valores digitados é:', soma)
print(f"A media dos valores digitados é: {media:.2f}")