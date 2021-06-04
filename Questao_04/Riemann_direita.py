from sympy import *
init_printing(pretty_print=true)
x = Symbol('x')


def h(a, b, n):
    resultado = (b - a) / n
    return resultado


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


def soma_riemann(valores_y, h, subintervalos):
    s = 0
    for c in range(1, subintervalos):
        s += (valores_y[c] * h)
    return s


def erro(valor_real, valor_encontrado):
    return valor_real - valor_encontrado


# Para 1 subintervalo:
h_1 = h(1, 4, 1)
integral = Integral(exp(x), (x, 1, 4)).doit().evalf()
valores_x_h1 = aplicando_h(1, 4, h_1)
valores_x_h1_aplicados = aplicando_x(valores_x_h1)
soma_h1 = soma_riemann(valores_x_h1_aplicados, h_1, 1)
erro_1 = erro(integral, soma_h1)
porcentagem_erro_1 = (erro_1 / integral) * 100

# Para 4 subintervalo:
h_4 = h(1, 4, 4)
valores_x_h4 = aplicando_h(1, 4, h_4)
valores_x_h4_aplicados = aplicando_x(valores_x_h4)
soma_h4 = soma_riemann(valores_x_h4_aplicados, h_4, 4).evalf()
erro_4 = erro(integral, soma_h4)
porcentagem_erro_4 = (erro_4 / integral) * 100

# Para 10 subintervalo:
h_10 = h(1, 4, 10)
valores_x_h10 = aplicando_h(1, 4, h_10)
valores_x_h10_aplicados = aplicando_x(valores_x_h10)
soma_h10 = soma_riemann(valores_x_h10_aplicados, h_10, 10).evalf()
erro_10 = erro(integral, soma_h10)
porcentagem_erro_10 = (erro_10 / integral) * 100

# Para 100 subintervalos:
h_100 = h(1, 4, 100)
valores_x_h100 = aplicando_h(1, 4, h_100)
valores_x_h100_aplicados = aplicando_x(valores_x_h100)
soma_h100 = soma_riemann(valores_x_h100_aplicados, h_100, 100).evalf()
erro_100 = erro(integral, soma_h100)
porcentagem_erro_100 = (erro_100 / integral) * 100


print('Para 1 subintervalo: ')
print('-' * 30)
print(f'Soma de Riemann = {soma_h1:.3f}')
print(f'Integral = {integral:.3f}')
print(f'Erro = {erro_1:.3f}')
print(f'Porcentagem do erro = {porcentagem_erro_1:.3f}%')
print('-' * 30)
print('Para 4 subintervalos: ')
print('-' * 30)
print(f'Soma de Riemann = {soma_h4:.3f}')
print(f'Erro = {erro_4:.3f}')
print(f'Porcentagem do erro = {porcentagem_erro_4:.3f}%')
print('-' * 30)
print('Para 10 subintervalos: ')
print('-' * 30)
print(f'Soma de Riemann = {soma_h10:.3f}')
print(f'Erro = {erro_10:.3f}')
print(f'Porcentagem do erro = {porcentagem_erro_10:.3f}%')
print('-' * 30)
print('Para 100 subintervalos: ')
print('-' * 30)
print(f'Soma de Riemann = {soma_h100:.3f}')
print(f'Erro = {erro_100:.3f}')
print(f'Porcentagem do erro = {porcentagem_erro_100:.3f}%')
