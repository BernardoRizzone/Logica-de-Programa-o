nome = str(input('Digite seu nome:'))
ano = int(input('\nInsira seu ano de nascimento:'))

idade = 2026 - ano

if idade>=16:
    print('Pode votar!')
else:
    print('Não pode votar!')

if idade>=18:
    print('Pode tirar a CNH')
else:
    print('Nao pode tirar a CNH')

print('Seu nome é', nome)
print('Ano de nascimento:', ano)
print('Idade:', idade)
