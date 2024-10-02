def luhn_check(card_num):
    # Convertir el número de tarjeta en una lista de dígitos y revertir el orden
    digits = [int(x) for x in str(card_num)][::-1]

    # Duplicar cada segundo dígito
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Sumar todos los dígitos
    total_sum = sum(digits)

    # Verificar si el total es divisible por 10
    return total_sum % 10 == 0

# Solicitar al usuario que ingrese el número de tarjeta
card_num = input("Por favor, ingrese el número de tarjeta: ")

# Validar si el número es válido
is_valid = luhn_check(card_num)

# Mostrar el resultado
print(f"El número de tarjeta {card_num} es {'válido' if is_valid else 'inválido'}")
