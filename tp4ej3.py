################
# Adrian Evaraldo - @chim20air
# TP1 Ejercicio 3 - Conversión de temperaturas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrenheit(centigrados):
    return (float(centigrados) * 1.8) + 32.0

def convertir_a_centigrados(fahrenheit):
    return (float(fahrenheit) - 32.0) / 1.8

if __name__ == "__main__":
    print(f"20°C son {convertir_a_fahrenheit(20)}°F")
    print(f"0.5°C son {convertir_a_fahrenheit(0.5)}°F")
    print(f"98°F son {convertir_a_centigrados(98)}°C")
    print(f"31.5°F son {convertir_a_centigrados(31.5)}°C")
    print(f"0°C son {convertir_a_fahrenheit(0)}°F")
    print(f"0°F son {convertir_a_centigrados(0)}°C")
