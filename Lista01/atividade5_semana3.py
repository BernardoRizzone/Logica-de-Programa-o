valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))

soma = valor1 +valor2
sub = valor1 - valor2

escolha = float(input('\nDigite 1 para soma, e 2 para a subtração:'))

if escolha == 1:
    print('A soma é:', soma)
elif escolha ==2:
    print('A subtração é:', sub)
else:
    print('A escolha para soma ou subtração foi errada')