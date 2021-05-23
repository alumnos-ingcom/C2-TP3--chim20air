################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 2 - Suma lenta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    if otro_numero > 0:
        for _ in range(otro_numero):
            numero = numero + 1
    elif otro_numero < 0:
        var = otro_numero * -1
        for _ in range(otro_numero * -1):
            numero -=1

    return numero

if __name__ == "__main__":
    print(f"Probemos con 4 y -3: {suma_lenta(4, -3)}")
    print(f"Probemos con 4 y 3: {suma_lenta(4, 3)}")
    print(f"Probemos con -4 y -3: {suma_lenta(-4, -3)}")
    print(f"Probemos con 4 y 0: {suma_lenta(4, 0)}")
    print(f"Probemos con 0 y -3: {suma_lenta(0, -3)}")
    print(f"Probemos con 0 y 3: {suma_lenta(0, 3)}")
