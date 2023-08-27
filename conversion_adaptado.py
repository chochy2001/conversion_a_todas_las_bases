# Valores de ejemplo
num = "101.101"  # Número a convertir
from_base = 2  # Base original
to_base = 10  # Base a la que se quiere convertir


# Definimos la función que se encargará de la conversión de bases
def convert_base(num, from_base, to_base):
    # Separamos la parte entera y decimal del número
    integer_part, _, decimal_part = num.partition('.')

    # Inicializamos la variable que almacenará el resultado de la parte entera
    integer_result = ''
    integer_part = int(integer_part, from_base)
    while integer_part > 0:
        remainder = integer_part % to_base
        if 0 <= remainder <= 9:
            integer_result = str(remainder) + integer_result
        else:
            integer_result = chr(ord('A') + remainder - 10) + integer_result
        integer_part //= to_base

    # Inicializamos la variable que almacenará el resultado de la parte decimal
    decimal_result = ''
    decimal_value = 0
    for i, digit in enumerate(decimal_part):
        if '0' <= digit <= '9':
            val = int(digit)
        else:
            val = ord(digit.upper()) - ord('A') + 10
        decimal_value += val * (from_base ** -(i + 1))

    # Limitamos a 5 decimales
    for _ in range(5):
        decimal_value *= to_base
        digit = int(decimal_value)
        if 0 <= digit <= 9:
            decimal_result += str(digit)
        else:
            decimal_result += chr(ord('A') + digit - 10)
        decimal_value -= digit

    # Mostramos el resultado
    result = integer_result + '.' + decimal_result
    print("Resultado:", result)


# Llamamos a la función con los valores de ejemplo
convert_base(num, from_base, to_base)
