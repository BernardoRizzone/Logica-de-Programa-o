media = 5
media_alunos = 0
cta = 0
ct = 0
ctr = 0
soma = 0


print('Digite [0] para parar de adicionar notas:')

while True:
    nota = float(input('Digite a nota:'))
    if nota == 0:
        break

    if nota >= media:
        cta = cta + 1

    if nota < media:
        ctr = ctr + 1
    soma = soma + nota
    ct = ct + 1
media_alunos = soma/ct
print('A quantidade de alunos que fizeram a prova:', ct)
print(f"A media dos alunos da sala foram: {media_alunos:.2f}")
print('A quantidade de alunos APROVADOS foram:', cta)
print('A quantidade de alunos REPROVADOS foram:', ctr)


