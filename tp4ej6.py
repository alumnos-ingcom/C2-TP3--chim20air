################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 6 - Maximo / minimo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep

def minimo(lista):
    """
    Devolver el valor minimo de una lista
    """
    mi = lista[0]
    for i in lista:
        if mi > i:
            mi = i
    return mi

def maximo(lista):
    """
    Devolver el valor maximo de una lista
    """
    ma = lista[0]
    for i in lista:
        if ma < i:
            ma = i
    return ma


def prueba():
    array = []
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se supone que le tenes que ingresar
un array de numeros y el programa devuelve con una 
funcion el valor menor y con otra el mayor
    Ingrese 1 para ingresar numeros para una lista o modificar la existente
    Ingrese 2 para ver la lista introducida
    Ingrese 3 para ver el valor maximo
    Ingrese 4 para ver el valor minimo
    Ingrese 5 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 5)
        if test == 1:
            array.clear()
            for i in range(inp.IngresoEntero("ingrese el largo de la lista")):
                array.append(inp.IngresoEntero(f"Ingrese el valor {i + 1}"))
        elif test == 2:
            if len(array) == 0:
                print("No hay valores de prueba")
                sleep(3)
                continue
            print(array)
            sleep(5)
        elif test == 3:
            if len(array) == 0:
                print("No hay valores de prueba")
                sleep(3)
                continue
            print(f"la lista es: {array}")
            print(f"la función maximo regresa: {maximo(array)}") 
            sleep(3)
        elif test == 4:
            if len(array) == 0:
                print("No hay valores de prueba")
                sleep(3)
                continue
            print(f"la lista es: {array}")
            print(f"la función minimo regresa: {minimo(array)}") 
            sleep(3)
        elif test == 5:
            break

if __name__ == "__main__":
    prueba()
