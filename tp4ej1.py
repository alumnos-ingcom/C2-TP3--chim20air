################
# Adrian Evaraldo - @chim20air
# ejercicio 1 - Ingreso de números enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """Manejo de error del tipo de entrada"""
    ingreso = input(mensaje + ">>> ")
    try:
        entero = int(ingreso)
    except ValueError as err:
        print(cantidad_reintentos)
        if cantidad_reintentos == 0:
            raise IngresoIncorrecto("Volve a primaria pibe") from err
        else:
            ingreso_entero_reintento(mensaje, cantidad_reintentos=cantidad_reintentos-1)
    return entero

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    if not valor_minimo < 

def IngresoEntero(mensaje):
    global valor_minimo, valor_maximo
    ingreso = input(mensaje + ">>> ")
    try:
        entero = int(ingreso)
    except ValueError:
        ingreso_entero_reintento("Pibe un entero te estoy pidiendo")
    else:
        check = ingreso_entero_restringido("Verificacion de rango") 
        return entero

if __name__ == "__main__":
    print(IngresoEntero("mandale mecha"))
