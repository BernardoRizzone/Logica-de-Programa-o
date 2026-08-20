produto = str(input('Digite o nome do produto:'))
compra = float(input('\nDigite o valor da compra:'))
venda = float(input('\nDigite o valor da venda:'))

conta1 = compra - venda
conta2 = venda - compra

if compra>venda:
    print('A venda do/a seu', produto, 'Teve prejuizo! O seu prejuizo foi de:', conta1,'$')
elif venda>compra:
    print('A venda do/a seu', produto, 'Teve lucro! O seu lucro foi de:', conta2,'$')
else:
    print(' Os valores são iguais!Não teve lucro ou prejuizo para o/a', produto,'.')

print('Preço de compra:', compra)
print('Preço de venda:', venda)
print('Nome do produto:', produto)