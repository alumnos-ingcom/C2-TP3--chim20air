################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 7 - Restas Sucesivas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep

def division_lenta(dividendo, divisor):
    """
    Escribir una función que mediante restas sucesivas, obtenga el
    valor del cociente y resto de dos números enteros.
    """
    cociente = 0

    while dividendo > divisor:
        dividendo = dividendo - divisor
        cociente += 1
    #lo que quede en el dividendo es el resto
    return cociente, dividendo

def prueba():
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se supone que le tenes que ingresar
dos numeros para ser divididos. El primero siendo el
dividendo y el segundo el divisor
    Ingrese 1 para realizar la division
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            cociente, resto = division_lenta(inp.IngresoEntero("ingrese el dividendo"),
                                            inp.IngresoEntero("ingrese el divisor"))
            print(f"El cociente es: {cociente}\n y el resto: {resto}")
            sleep(3)
        elif test == 2:
            break

if __name__ == "__main__":
    prueba()
