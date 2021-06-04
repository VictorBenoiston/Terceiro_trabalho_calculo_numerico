x = [1960, 1975, 1990, 2000, 2010]
y = [316, 330, 356, 367, 386]


def somatorio(lista):
    somatorio = 0
    for item in lista:
        somatorio += item
    return somatorio


def potencia(lista, potencia):
    lista_resultante = []
    for item in lista:
        elemento = item ** potencia
        lista_resultante.append(elemento)
    return lista_resultante


def x_vezes_y(lista_x, lista_y):
    valores_x_vezes_y = []
    for c in range(0, len(lista_x)):
        elemento = lista_x[c] * lista_y[c]
        valores_x_vezes_y.append(elemento)
    return valores_x_vezes_y


def media(lista):
    total = 0
    for item in lista:
        total += item
    media = total / len(lista)
    return media


def SQreg(gx, y_barra):
    valores_sqreg = []
    for c in gx:
        elemento = (c - y_barra) ** 2
        valores_sqreg.append(elemento)
    return valores_sqreg


def SQtot(yi, y_barra):
    valores_sqtot = []
    for c in yi:
        elemento = (c - y_barra) ** 2
        valores_sqtot.append(elemento)
    return valores_sqtot


def R2(sqreg, sqtot):
    total = sqreg/sqtot
    return total


somatorio_x = somatorio(x)
somatorio_y = somatorio(y)
x_quadrado = potencia(x, 2)
somatorio_x_quadrado = somatorio(x_quadrado)
x_cubo = potencia(x, 3)
somatorio_x_cubo = somatorio(x_cubo)
x_quarta = potencia(x, 4)
somatorio_x_quarta = somatorio(x_quarta)
x_y = x_vezes_y(x, y)
somatorio_xy = somatorio(x_y)
n = len(x)
x_quadrado_y = x_vezes_y(x_quadrado, y)
somatorio_x_quadrado_y = somatorio(x_quadrado_y)

matriz_resultante = [[n, somatorio_x, somatorio_x_quadrado, somatorio_y], [somatorio_x, somatorio_x_quadrado, somatorio_x_cubo, somatorio_xy], [somatorio_x_quadrado, somatorio_x_cubo, somatorio_x_quarta, somatorio_x_quadrado_y]]

# Resolendo a matriz:
# Pivô (1) = 5
mL2, mL3 = 1987, 3948485

# Nova linha 2 = L2 - mL2 * L1

# Primeira iteração:
nova_matriz_1 = [[matriz_resultante[0]], [], []]

for c in range(0, len(matriz_resultante[0])):
    elemento_1 = (matriz_resultante[1][c] - (mL2 * matriz_resultante[0][c]))
    nova_matriz_1[1].append(elemento_1)
    elemento_2 = (matriz_resultante[2][c] - (mL3 * matriz_resultante[0][c]))
    nova_matriz_1[2].append(elemento_2)

# Pivô (2) = 1580
mL3 = (313595/79)
# Segunda iteração:
nova_matriz_2 = [nova_matriz_1[0], [nova_matriz_1[1]], []]

for c in range(0, len(matriz_resultante[0])):
    elemento = (nova_matriz_1[2][c] - (mL3 * nova_matriz_1[1][c]))
    nova_matriz_2[2].append(elemento)

c = nova_matriz_2[2][-1] / nova_matriz_2[2][-2]
b = (nova_matriz_2[1][0][-1] - (nova_matriz_2[1][0][2] * c)) / (nova_matriz_2[1][0][1])
a = (nova_matriz_2[0][0][-1] - ((nova_matriz_2[0][0][1] * b) + nova_matriz_2[0][0][2] * c)) / 5


def g(x, a, b, c):
    resultado = (c * x ** 2) + (b * x) + a
    return resultado


def valores_aplicados(valores, a, b, c):
    lista_valores_aplicados = []
    for valor in valores:
        valor_aplicado = g(valor, a, b, c)
        lista_valores_aplicados.append(valor_aplicado)
    return lista_valores_aplicados


y_barra = media(y)
g_x_aplicado = valores_aplicados(x, a, b, c)
sqreg = SQreg(g_x_aplicado, y_barra)
somatorio_sqreg = somatorio(sqreg)
sqtot = SQtot(y, y_barra)
somatorio_sqtot = somatorio(sqtot)
r2 = R2(somatorio_sqreg, somatorio_sqtot)


print('ESTATÍSTICA'.center(30))
print('-' * 30)
print(f'Somatório de x = {somatorio_x:.3f}')
print(f'Somatório de y = {somatorio_y:.3f}')
print(f'Somatório X.Y = {somatorio_xy:.3f}')
print(f'Somatório x² = {somatorio_x_quadrado:.3f}')
print(f'Somatório x³ = {somatorio_x_cubo:.3f}')
print(f'Somatório x^4 = {somatorio_x_quarta}')
print(f'Somatório x²Y = {somatorio_x_quadrado_y:.3f}')
print(f'Valor de R² = {r2:.4f}')
print('-' * 30)
print(f'A equação é: g(x) = {c}X²  {b}X + {a}')
print('-' * 30)
print(f'A estimativa da concentração em 2015 é de {g(2015, a, b, c):,.3f} ppm')
print(f'A estimativa da concentração em 2020 é de {g(2020, a, b, c):,.3f} ppm')
