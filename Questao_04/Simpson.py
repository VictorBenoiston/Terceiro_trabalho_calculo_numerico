from sympy import *
init_printing(pretty_print=true)
x = Symbol('x')

def f(x):
    return exp(x)


def aplicando_h(a, b, h):
    lista = [a]
    elemento = 0
    while True:
        if elemento < b:
            elemento = lista[-1] + h
            lista.append(elemento)
        else:
            break
    return lista


def aplicando_x(lista_x):
    lista_x_aplicado = []
    for c in lista_x:
        elemento = f(c)
        lista_x_aplicado.append(elemento)
    return lista_x_aplicado


def isimpar(number):
    if (number % 2) != 0:
        return true
    else:
        return false


def somatorio(lista):
    somatorio = 0
    for item in lista:
        somatorio += item
    return somatorio


def simpson(x0, xn, n_intervalos):
    # if n_intervalos == 1:
    #     i2 = (h / 3) * (y[0] + (4 * y[1]) + y[2])
    #     return i2
    h = (xn - x0) / n_intervalos
    soma = f(x0) + f(xn)
    for c in range(1, n_intervalos):
        k = x0 + (c * h)
        if isimpar(c):
            soma = soma + 4 * f(k)
        else:
            soma = soma + 2 * f(k)
    soma_final = soma * (h/3)
    return soma_final


def erro(valor_real, valor_soma):
    erro = valor_soma - valor_real
    return erro


# # Para 1 subintervalo:
integral = Integral(exp(x), (x, 1, 4)).doit().evalf()
soma_simpson_1 = simpson(1, 4, 1).evalf()
erro_1 = erro(integral, soma_simpson_1)
porcentagem_erro_1 = (erro_1 / integral) * 100

# # Para 4 subintervalo:
soma_simpson_4 = simpson(1, 4, 4).evalf()
erro_4 = erro(integral, soma_simpson_4)
porcentagem_erro_4 = (erro_4 / integral) * 100

# Para 10 subintervalo:
soma_simpson_10 = simpson(1, 4, 10).evalf()
erro_10 = erro(integral, soma_simpson_10)
porcentagem_erro_10 = (erro_10 / integral) * 100

# Para 100 subintervalo:
soma_simpson_100 = simpson(1, 4, 100).evalf()
erro_100 = erro(integral, soma_simpson_100)
porcentagem_erro_100 = (erro_100 / integral) * 100


# print('Para 1 subintervalo: ')
# print('-' * 30)
print(f'1/3 de Simpson = {soma_simpson_1:.3f}')
print(f'Integral = {integral:.3f}')
print(f'Erro = {erro_1:.3f}')
print(f'Porcentagem do erro = {porcentagem_erro_1:.3f}%')
print('-' * 30)
print('Para 4 subintervalos: ')
print('-' * 30)
print(f'1/3 de Simpson = {soma_simpson_4:.3f}')
print(f'Erro = {erro_4:.3f}')
print(f'Porcentagem do erro = {porcentagem_erro_4:.3f}%')
print('-' * 30)
print('Para 10 subintervalos: ')
print('-' * 30)
print(f'1/3 de Simpson = {soma_simpson_10:.3f}')
print(f'Erro = {erro_10:.3f}')
print(f'Porcentagem do erro = {porcentagem_erro_10:.3f}%')
print('-' * 30)
print('Para 100 subintervalos: ')
print('-' * 30)
print(f'1/3 de Simpson = {soma_simpson_100:.3f}')
print(f'Erro = {erro_100:.3f}')
print(f'Porcentagem do erro = {porcentagem_erro_100:.3f}%')

