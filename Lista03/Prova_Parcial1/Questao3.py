print(' Vamos calcular a distancia entre dois pontos quaisequer do plano cartesiano. P(x1, y1) e Q(x2, y2).')
X1 = int(input('Digite o valor de x1:'))
Y1 = int(input('Digite o valor de y1:'))
X2 = int(input('Digite o valor de x2:'))
Y2 = int(input('Digite o valor de y2:'))

distancia = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2) ** 0.5
print('A distancia entre os pontos P e Q é de:', distancia)