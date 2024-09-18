# Ejercicio 5, Programa para evaluar el rendimiento de empleados en Corpoelec

# Definir la cantidad base de dinero
cantidad_base = 2400

# Solicitamos al usuario que ingrese su puntuación
puntuacion = float(input("Por favor, ingresa tu puntuación (0.0, 0.4, 0.6 o más): "))

# Inicializar variables para el nivel de rendimiento y la cantidad a recibir
nivel_rendimiento = ""
cantidad_a_recibir = 0

# Evaluar la puntuación y determinar el nivel de rendimiento
if puntuacion < 0.4:
    nivel_rendimiento = "Inaceptable"
elif puntuacion < 0.6:
    nivel_rendimiento = "Aceptable"
else:
    nivel_rendimiento = "Meritorio"

# Calcular la cantidad a recibir
cantidad_a_recibir = cantidad_base * puntuacion

# Mostrar el resultado al usuario
print(f"Nivel de rendimiento: {nivel_rendimiento}")
print(f"Cantidad a recibir: {cantidad_a_recibir} €")
