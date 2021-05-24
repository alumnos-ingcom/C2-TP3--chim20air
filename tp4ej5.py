################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 5 - Numeros positivos y negativos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp

def signo(numero):
    """
    Escribir una función que reciba un número e indique si
    el mismo es positivo, negativo o cero.
    La función devolvera:

    * 1 si es positivo
    * 0 si es cero
    * -1 si es negativo
    """
    #Estoy en duda de si querés que devuelva un string o 
    #si queres que imporma algo en la terminal

    if numero > 0:
        ret = 1
    elif numero == 0:
        ret = 0
    else:
        ret = -1

    return ret

def prueba():
    print('\033[2J')
    print("""
En este ejercicio, se supone que le tenes que ingresar
un numero y el programa devuelve:
* Retorna `-1` si es negtivo
* Retorna `0` si es cero
* Retorna `1` si es positivo
        """)

    while True:
        print("""
Ingrese 1 para continuar con la prueba
Ingrese 2 para terminar la prueba""")
        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            print(f"la función de signo regresa: {signo(inp.IngresoEntero('Ingresa el numero'))}") 
        elif test == 2:
            break

if __name__ == "__main__":
    prueba()
