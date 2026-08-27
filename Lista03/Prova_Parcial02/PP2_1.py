soma = 0
ct=0
ctm = 0
maior = 20
print('Digite [0] para parar de digitar os numeros')

while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break

    if valor > maior:
        ctm += 1

    soma = soma + valor
    ct+=1
media = soma/ct
print('Os quantidade de valores digitados foram:', ct)
print('A soma dos valores digitados é:', soma)
print(f"A media dos valores é: {media:.2f}")
print('A quantidade de valores maior do que 20 foram:', ctm)
