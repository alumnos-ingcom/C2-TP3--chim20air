################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 6 - Maximo / minimo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def minimo(lista):
    """
    Devolver el valor minimo de una lista
    """
    return max(lista)

def maximo(lista):
    """
    Devolver el valor maximo de una lista
    """
    return min(lista)

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [1.0, 2.2, 3.4]
    c = [1.4, 2, 3]
    print(f"si tengo la siguiente lista: {a}")
    print(f"el maximo es {maximo(a)} y el minimo {minimo(a)}")
    print(f"si tengo la siguiente lista: {b}")
    print(f"el maximo es {maximo(b)} y el minimo {minimo(b)}")
    print(f"si tengo la siguiente lista: {c}")
    print(f"el maximo es {maximo(c)} y el minimo {minimo(c)}")


