def suma_lista(input_lista):
    suma_total = 0
    for elemento in input_lista:
        suma_total += elemento
    return suma_total

lista = [10, 9, 8, 7, 6, 5]
resultado = suma_lista(lista)
print(resultado)