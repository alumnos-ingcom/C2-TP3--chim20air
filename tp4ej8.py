################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 8 - Ordenar 3 valores
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep


def ordenar_mayor_a_menor(uno, dos, tres):
    l = [uno, dos, tres]
    for _ in range(len(l)):
        changed = False
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                changed = True
        if not changed:
            break

    return l

def ordenar_menor_a_mayor(uno, dos, tres):
    l = [uno, dos, tres]
    for _ in range(len(l)):
        changed = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                changed = True
        if not changed:
            break

    return l

def prueba():
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se supone que le tenes que ingresar
3 numeros y el programa los devuelve de manera ordenada
    Ingrese 1 para ordenar de menor a mayor
    Ingrese 2 para ordenar de mayor a menor
    Ingrese 3 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 3)
        if test == 1:
            print(f"""la función que ordena de menor a mayor regresa: {ordenar_menor_a_mayor(
                    inp.IngresoEntero('ingrese el primer valor'),
                    inp.IngresoEntero('ingrese el segundo valor'),
                    inp.IngresoEntero('ingrese el tercer valor'))}""") 
            sleep(10)
        elif test == 2:
            print(f"""la función de orden de mayor a menor regresa: {ordenar_mayor_a_menor(
                    inp.IngresoEntero('ingrese el primer valor'),
                    inp.IngresoEntero('ingrese el segundo valor'),
                    inp.IngresoEntero('ingrese el tercer valor'))}""") 
            sleep(10)
        elif test == 3:
            break
if __name__ == "__main__":
    prueba()
