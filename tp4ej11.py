################
# Adrian Evaraldo - @chim20air
# Ejercicio 11 - Palindromo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep

def es_palindromo(texto):
    retorno = True
    for letra in range(len(texto)):
        if texto[letra] != texto[-letra - 1]:
            retorno = False
            break
    return retorno

def prueba():
    while True:
        print('\033[2J')
        print("""
En este ejercicio, se supone que le tenes que ingresar
un texto y el programa indica si es o no capicua
    Ingrese 1 para ingresar el texto de prueba
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            print(f"la función regresa: {es_palindromo(input('El texto de prueba >>> '))}") 
            sleep(3)
        elif test == 2:
            break

if __name__ == "__main__":
    prueba()
