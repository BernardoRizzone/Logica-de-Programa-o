ct_voto1 = 0
ct_voto2 = 0
ct_voto3 = 0
ct_voto5 = 0
ct_voto6 = 0



print('VOTE [1] para joão\n VOTE[2] para Carlos\n VOTE[3] para Pedro\n VOTE[5] para anular\n VOTE[6] deixar em branco\n DIGITE [0] para sair:')

while True:
    voto = int(input('Digite o seu voto:'))
    if voto == 0:
        break
    elif voto == 1:
        ct_voto1 += 1
    elif voto == 2:
        ct_voto2 += 1
    elif voto == 3:
        ct_voto3 += 1
    elif voto == 5:
        ct_voto5 += 1
    elif voto == 6:
        ct_voto6 += 1
    else:
        print('VOTO INVALIDO')

print('O numero de votos no candidato 1:', ct_voto1)
print('O numero de votos no candidato 2:', ct_voto2)
print('O numero de votos no candidato 3:', ct_voto3)
print('O numero de votos nulos:', ct_voto5)
print('O numero de votos em branco:', ct_voto6)

