# Ejercicio 1, programa para determinar si una persona es mayor de edad

# Solicitamos la edad al usuario y convertir la entrada a un entero
edad = int(input("Por favor, ingresa tu edad: "))

# Verificamos si la edad es 18 años o más
if edad >= 18:
    # Si la condición es verdadera, el usuario es mayor de edad
    print("Eres mayor de edad.")
else:
    # Si la condición es falsa, el usuario no es mayor de edad
    print("No eres mayor de edad.")
