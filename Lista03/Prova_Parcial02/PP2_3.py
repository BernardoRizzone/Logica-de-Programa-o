soma_par = 0
soma_impar = 0
ct = 0
ctp = 0
cti = 0

print('Digite [0] para parar de digitar os valores')

while True:
    valor = int(input('Digite um valor inteiro: '))
    if valor == 0:
        break

    if valor % 2 ==0:
        soma_par = soma_par + valor
        ctp = ctp + 1

    if valor % 2 != 0:
        soma_impar = soma_impar + valor
        cti = cti +1

media_par = soma_par/ctp
media_impar = soma_impar/cti
soma_total = soma_par + soma_impar
ct = cti + ctp

print(f"A media dos numeros pares é: {media_par:.2f}")
print(f"A media dos numeros imapares é: {media_impar:.2f}")
print('A quantidade de valores digitados foram:', ct)
print('A soma dos valores digitados foram:', soma_total)