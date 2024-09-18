# Ejercicio 2, programa para calcular el área de un rectángulo y verificar condiciones

# Solicitamos la base del rectángulo al usuario y convertirla a un número flotante
base = float(input("Por favor, ingresa la base del rectángulo: "))

# Solicitamos la altura del rectángulo al usuario y convertirla a un número flotante
altura = float(input("Por favor, ingresa la altura del rectángulo: "))

# Calculamos el área del rectángulo usando la fórmula a = b * h
area = base * altura

# Mostramos el área calculada
print(f"El área del rectángulo es: {area}")

# Verificamos si el área es mayor a 40 y la altura es mayor a 10
if area > 40 and altura > 10:
    # Si ambas condiciones se cumplen, mostrar un mensaje personalizado
    print("¡Increíble! El área es mayor a 40 y la altura es mayor a 10.")
else:
    # Si alguna de las condiciones no se cumple, mostrar un mensaje alternativo
    print("El área o la altura no cumplen con las condiciones especificadas.")
