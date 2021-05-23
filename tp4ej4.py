################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 4 - Comparación de numeros
# UNRN Andina - Introducción a la Ingenieria en Computación
################



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

if __name__ == "__main__":
    print(f"1 y 2 devuelve: {compara(1, 2)}")
    print(f"1.0 y 2.0 devuelve: {compara(1.0, 2.0)}")
    print(f"1.0 y 2 devuelve: {compara(1.0, 2)}")
    print(f"3 y 2 devuelve: {compara(3, 2)}")
    print(f"2 y 2 devuelve: {compara(2, 2)}")



