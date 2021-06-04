import numpy as np
x = [1970, 1980, 1991, 1996, 2000, 2010]
y = [132165, 151326, 179323, 203302, 226542, 249633]

ln_y = []

for item in y:
    log_y = np.log(item)
    ln_y.append(log_y)


def somatorio(lista):
    somatorio = 0
    for item in lista:
        somatorio += item
    return somatorio


def x_vezes_y(lista_x, lista_y):
    valores_x_vezes_y = []
    for c in range(0, len(lista_x)):
        elemento = lista_x[c] * lista_y[c]
        valores_x_vezes_y.append(elemento)
    return valores_x_vezes_y


def quadrado(x):
    lista_quadrados = []
    for item in x:
        elemento = item ** 2
        lista_quadrados.append(elemento)
    return lista_quadrados


def a(x, somatorio_x, somatorio_y, somatorio_xy, somatorio_x_quadrado):
    n = len(x)
    resultado = ((n * somatorio_xy) - (somatorio_x * somatorio_y)) / ((n * somatorio_x_quadrado) - (somatorio_x ** 2))
    return resultado


def b(x, somatorio_x, somatorio_y, somatorio_xy, somatorio_x_quadrado):
    n = len(x)
    resultado = ((somatorio_x * somatorio_xy) - (somatorio_y * somatorio_x_quadrado)) / ((somatorio_x ** 2) - (n * somatorio_x_quadrado))
    return resultado


def g(x, a, b):
    resultado = b * np.exp(a * x)
    return resultado


def media(lista):
    total = 0
    for item in lista:
        total += item
    media = total / len(lista)
    return media


def valores_aplicados(valores):
    lista_valores_aplicados = []
    for valor in valores:
        valor_aplicado = g(valor, valor_a, b_real)
        lista_valores_aplicados.append(valor_aplicado)
    return lista_valores_aplicados


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
somatorio_y = somatorio(ln_y)
valores_x_vezes_y = x_vezes_y(x, ln_y)
somatorio_x_vezes_y = somatorio(valores_x_vezes_y)
x_ao_quadrado = quadrado(x)
somatorio_x_quadrado = somatorio(x_ao_quadrado)
valor_a = a(x, somatorio_x, somatorio_y, somatorio_x_vezes_y, somatorio_x_quadrado)
valor_b = b(x, somatorio_x, somatorio_y, somatorio_x_vezes_y, somatorio_x_quadrado)
b_real = np.exp(valor_b)
y_barra = media(ln_y)
g_x_aplicado = valores_aplicados(x)
sqreg = SQreg(g_x_aplicado, y_barra)
somatorio_sqreg = somatorio(sqreg)
sqtot = SQtot(y, y_barra)
somatorio_sqtot = somatorio(sqtot)
r2 = R2(somatorio_sqreg, somatorio_sqtot)


print('ESTATÍSTICA'.center(30))
print('-' * 30)
print(f'Somatório de x = {somatorio_x}')
print(f'Somatório de y = {somatorio_y}')
print(f'Somatório X.Y = {somatorio(valores_x_vezes_y)}')
print(f'Somatório X² = {somatorio_x_quadrado}')
print(f'Valor de a = {valor_a:.3f}')
print(f'Valor de b = {b_real}')
print(f'Valor de y médio = {y_barra:.3f}')
print(f'Valor de R² = {r2:.4f}')
print('-' * 30)
print(f'A equação é: g(x) = {valor_a:.3f}X + {b_real}')
print('-' * 30)
print(f'Estimativa população em 2003 = {g(2003, valor_a, b_real):,.3f}')
print(f'Estimativa população em 2020 = {g(2020, valor_a, b_real):,.3f}')
