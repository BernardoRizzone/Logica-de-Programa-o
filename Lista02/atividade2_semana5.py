ct = 0
somador = 0


print('Digite -1 para sair:')
disciplina = str(input('Digite o nome do disciplina: '))

while True:
    nota = float(input('Digite as notas do aluno: '))
    if nota == -1:
        break
    somador += nota
    ct+=1
media = somador / ct
print('Quantidade de notas:', ct)
print(f"A media foi:' {media:.2f}")
print('A soma das notas é:', somador)
print('A disciplina é:', disciplina)
