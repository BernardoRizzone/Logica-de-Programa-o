nota1 = float(input('Digite sua primeira nota, em caso de numero decimal use o "." inves da ",":'))
nota2= float(input('\nDigite sua segunda nota, em caso de numero decimal use o "." inves da ",":'))

media = (nota1+nota2)/2

print('\nSua media foi:', f"{media:.2f}")

if media >=5:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')