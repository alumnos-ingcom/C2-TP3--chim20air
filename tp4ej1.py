################
# Adrian Evaraldo - @chim20air
# ejercicio 1 - Ingreso de números enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class NoMoreReintentos(Exception):
    """Esta es la excepcion para cuando se terminan la cantidad de reintentos"""
    pass

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """Manejo de error del tipo de entrada"""
    ingreso = input(mensaje + ">>> ")
    try:
        entero = int(ingreso)
    except ValueError as err:
        print(cantidad_reintentos)
        if cantidad_reintentos == 0:
            raise NoMoreReintentos("Volve a primaria pibe")
        else:
            ingreso_entero_reintento(mensaje, cantidad_reintentos=cantidad_reintentos-1)
    return entero

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    pass

def IngresoEntero(mensaje):
    ingreso = input(mensaje + ">>> ")
    try:
        entero = int(ingreso)
    except ValueError as err:
        ingreso_entero_reintento("Pibe un entero te estoy pidiendo")
    return entero

if __name__ == "__main__":
    print(IngresoEntero("mandale mecha"))
