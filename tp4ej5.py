################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 5 - Numeros positivos y negativos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    """
    Escribir una función que reciba un número e indique si
    el mismo es positivo, negativo o cero
    """
    #Estoy en duda de si querés que devuelva un string o 
    #si queres que imporma algo en la terminal

    if numero > 0:
        ret = "numero positivo"
    elif numero == 0:
        ret ="numero es cero"
    else:
        ret = "numero negativo"

    return ret

if __name__ == "__main__":
    print(f"5 es: {signo(5)}")
    print(f"-5 es: {signo(-5)}")
    print(f"0 es: {signo(0)}")
    print(f"5.2 es: {signo(5.2)}")
