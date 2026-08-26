menor_valor = 99999
ct = 0
soma = 0

print("Digite o [0] para sair:")
while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break

    if menor_valor > valor:
        menor_valor = valor
    ct += 1
    soma = soma +valor
media = soma/ct
print('O menor valor é:', menor_valor)
print('A quantidade de valores digitados foi:', ct)
print('A soma dos valores digitados é:', soma)
print(f"A media dos valores digitados é: {media:.2f}")