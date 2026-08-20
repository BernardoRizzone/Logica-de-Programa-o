print('Escolha a opção aritmetica desejada, use os simbolos +, -, *, / para somar, subtrair, multiplicar e dividir respectivamente.')
simbolo = str(input('Digite o simbolo da operação desejada:'))

if simbolo == '+':
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero:'))
    resultado = num1 + num2
    print('O resultado da soma é:', resultado)

elif simbolo == '-':
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero:'))
    resultado = num1 - num2
    print('O resultado da subtração é:', resultado)

elif simbolo == '*':
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero:'))
    resultado = num1 * num2
    print('O resultado da multiplicação é:', resultado)

elif simbolo == '/':
    num1 = float(input('Digite o primeiro numero:'))
    num2 = float(input('Digite o segundo numero:'))
    if num2 == 0:
        print('Erro: Divisão por zero não é permitida.')
    else:
        resultado = num1 / num2
        print('O resultado da divisão é:', resultado)

else:
    print('Erro: Operação inválida. Por favor, use +, -, *, ou /.')