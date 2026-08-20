numero1 = float(input('Digite um numero:'))
numero2 = float(input('Digite outro numero:'))

if numero1>numero2:
    print('O primeiro numero digitado é maior:', numero1, 'o segundo:', numero2 )
elif numero1<numero2:
    print('O segundo numero digitado é o maior:', numero2, 'o primeiro:', numero1)
else:
    print('Os dois numeros sao iguais:', numero1, numero2)