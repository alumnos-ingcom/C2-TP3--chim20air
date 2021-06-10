################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 4 - Comparación de numeros
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp

def compara(numero, otro_numero):
    """
    Escribir una función que reciba dos valores y retorne:
        * Retornar `-1` si el primero es menor que el segundo
        * Retornar `0` si son iguales
        * Retornar `1` si el primero es mayor que el segundo
    """
    if numero < otro_numero:
        ret = -1
    elif numero == otro_numero:
        ret = 0
    else:
        ret = 1

    return ret

def prueba():
    print('\033[2J')
    print("""
En este ejercicio, se supone que le tenes que ingresar
dos numeros y el programa devuelve:
    * Retorna `-1` si el primero es menor que el segundo
    * Retorna `0` si son iguales
    * Retorna `1` si el primero es mayor que el segundo
            """)
    while True:
        print("""
    Ingrese 1 para continuar con la prueba
    Ingrese 2 para terminar la prueba""")
        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            ingreso1 = inp.IngresoEntero('Ingresa el primer numero')
            ingreso2 = inp.IngresoEntero('Ingresa el segundo numero')
            print(f"la función de compara regresa: {compara(ingreso1, ingreso2)}")
        elif test == 2:
            break

if __name__ == "__main__":
    prueba()
