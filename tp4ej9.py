################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 9 - Numeros primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep

def es_primo(numero):
    """
    Algoritmo para detectar si un numero es o no primo
    """
    count = 0
    for i in range(1, numero):
        if numero % i == 0:
            count += 1
            if count == 2:
                break
    if count == 1:
        ret = True
    else:
        ret = False

    return ret

def prueba():
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se supone que le tenes que ingresar
un numero y el programa indica si es o no primo
    Ingrese 1 para ingresar el numero de prueba
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            ingreso = inp.IngresoEntero('El numero de prueba')
            funcion = es_primo(ingreso)
            print(f"la función regresa: {funcion}") 
            sleep(5)
        elif test == 2:
            break
if __name__ == "__main__":
    prueba()
