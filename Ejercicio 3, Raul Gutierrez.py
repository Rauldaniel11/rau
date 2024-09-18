# Ejercicio 3, Programa para verificar la coincidencia de contraseñas

# Almacenar la contraseña en una variable
contraseña_guardada = "Ivannateamo"

# Solicitar al usuario que ingrese la contraseña
contraseña_usuario = input("Por favor, ingresa la contraseña: ")

# Comparar las contraseñas ignorando mayúsculas y minúsculas
if contraseña_usuario.lower() == contraseña_guardada.lower():
    # Si coinciden, mostrar un mensaje de éxito
    print("Contraseña correcta. Acceso concedido.")
else:
    # Si no coinciden, mostrar un mensaje de error
    print("Contraseña incorrecta. Acceso denegado.")
