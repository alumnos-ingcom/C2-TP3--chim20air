################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 10 - Factores Primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from tp4ej9 import es_primo
from time import sleep

def factores_primos(numero):
    """
    Escribir una función que retorne una `tupla` con factores
    primos de un numero entero positivo.
    """
    factores = [1]
    for i in range(1, numero):
        if numero % i == 0:
            if es_primo(i):
                factores.append(i)

    return tuple(factores)

def prueba():
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se supone que le tenes que ingresar
un numero y el programa devuelve los factores primos
del numero ingresado
    Ingrese 1 para ingresar el numero de prueba
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            ingreso = inp.IngresoEntero('El numero de prueba')
            print(f"la función regresa: {factores_primos(ingreso)}") 
            sleep(5)
        elif test == 2:
            break
if __name__ == "__main__":
    prueba()
