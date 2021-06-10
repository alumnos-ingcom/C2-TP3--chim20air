################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 3 - Conversión de temperaturas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp

def convertir_a_fahrenheit(centigrados):
    return (centigrados * 1.8) + 32.0

def convertir_a_centigrados(fahrenheit):
    return (fahrenheit - 32.0) / 1.8

def prueba():
    print('\033[2J')
    print("""En este ejercicio, se supone que le tenes que poner un
            numero en grados centigrados y que se convierta a 
            fahrenheit, o viceversa""")
    while True:
        print("""
En este ejercicio, se supone que le tenes que poner un
numero en grados centigrados y que se convierta a 
fahrenheit, o viceversa
    Ingrese 1 para pasar a centigrados
    Ingrese 2 para pasar a fahrenheit
    Ingrese 3 para terminar la prueba""")
        test = inp.ingreso_entero_restringido("ingrese opción", 1, 3)
        if test == 1:
            ingreso = inp.IngresoEntero('Ingresa un numero en °F')
            print(f"la función de convertir_a_centigrados regresa: {convertir_a_centigrados(ingreso)}") 
        elif test == 2:
            ingreso = inp.IngresoEntero('Ingresa un numero en °C')
            print(f"la función de convertir_a_fahrenheit regresa: {convertir_a_fahrenheit(ingreso)}") 
        elif test == 3:
            break

if __name__ == "__main__":
    prueba()
