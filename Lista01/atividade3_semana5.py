ct = 0
somador =0

print('Digite 0 para sair:')

while True:
    numero = int(input('Digite um numero:'))
    if numero == 0:
        break
    par = numero % 2
    if par == 0:
        somador = somador + numero
        ct+=1
media = somador / ct
print('A media dos numeros é:', media)
