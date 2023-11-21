def suma_lista(input_lista):
    suma_total = 0
    for elemento in input_lista:
        suma_total += elemento
    return suma_total

def multiplicar_lista(input_lista):
    multiplicar_total = 0 
    for valor in input_lista:
        multiplicar_total *= valor
    return multiplicar_total

lista = [10, 9, 8, 7, 6, 5]
resultado_suma = suma_lista(lista)
resultado_multiplicar = multiplicar_lista(lista)
print(resultado_suma)
print(resultado_multiplicar)
