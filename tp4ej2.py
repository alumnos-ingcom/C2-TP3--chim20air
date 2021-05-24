################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 2 - Suma lenta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import IngresoEntero as ie

def suma_lenta(numero, otro_numero):
    """
    Escribir una función que haga la suma entre dos números enteros sin hacer
    la operación de manera directa. Esto quiere decir que para hacer la suma
    entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.
    """
    if otro_numero > 0:
        for _ in range(otro_numero):
            numero = numero + 1
    elif otro_numero < 0:
        var = otro_numero * -1
        for _ in range(otro_numero * -1):
            numero -=1

    return numero

def prueba():
    print('\033[2J')
    print("""En este ejercicio, se supone que le tenes que poner 2 numeros y que
            se sumen lentamente. i.e. que se sumen de a uno""")
    while True:
        print("Para frenar la prueba, el primer numero tiene que ser 256")
        a = ie("Vamos con el primer numero")
        if a == 256:
            break
        print(f"la función de suma lenta regresa: {suma_lenta(a, ie('Vamos con el segundo numero'))}") 

if __name__ == "__main__":
    prueba()
