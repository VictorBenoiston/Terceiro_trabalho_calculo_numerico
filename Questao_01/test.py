
def h(a, b, n):
    resultado = (b - a) / n
    return resultado


def f(x):
    return 1/x


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


def simpson(y, h):
    i2 = (h / 3) * (y[0] + (4 * y[1]) + y[2])
    return i2


integral = 1.0986
test_h = h(1, 3, 2)
print(test_h)
test_lista_h = aplicando_h(1, 3, test_h)
print(test_lista_h)
test_aplicado = aplicando_x(test_lista_h)
print(test_aplicado)
test_final = simpson(test_aplicado, test_h)
print(test_final)

