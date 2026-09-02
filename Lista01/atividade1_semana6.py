ctm = 0
ctf = 0
maior =-1
menor =9
somador =0
ctg =0

print('Digite a altura em m, e [f] para genero feminino e [m] para genero masculino. Digite [0] para parar de digitar')


while True:
    altura = float(input('Digite a altura em m:'))
    print('Altura digitada:', altura)
    if altura == 0:
        break
    elif altura > maior:
        maior = altura
    elif altura < menor:
        menor = altura
    somador = somador + altura

    genero = str(input('Digite o genero, e [s] para sair:'))
    print('Genero digitado:', genero)
    if genero == 's':
        break

    while genero not in ['s','m','f']:
        genero = str(input('ERRO! Digite somente as letras [m], [f], [s] para sair:'))

    if genero == 'm':
        ctm += 1
    else:
        ctf += 1

ctg = ctm +ctf
media = somador/ctg


print('A maior altura é:', maior)
print('A menor altura é:', menor)
print('O numero de generos masculinos é:', ctm)
print('O numero de generos femininos é:', ctf)
print(f'A media das alturas somadas é: {media:.2f}')