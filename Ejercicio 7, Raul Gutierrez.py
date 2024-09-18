##Ejercicio 7,  Programa de calificaciones
# Función para determinar la calificación
def obtener_calificacion(nota):
    if 90 <= nota <= 100:
        return 'A'
    elif 80 <= nota < 90:
        return 'B'
    elif 70 <= nota < 80:
        return 'C'
    elif 60 <= nota < 70:
        return 'D'
    elif 0 <= nota < 60:
        return 'F'
    else:
        return None  # Para notas fuera del rango válido

# Solicitamos la calificación al usuario
try:
    calificacion = float(input("Ingrese la calificación (0-100): "))
    
    # Obtener la letra correspondiente
    letra_calificacion = obtener_calificacion(calificacion)
    
    if letra_calificacion is not None:
        print(f"La calificación correspondiente es: {letra_calificacion}")
    else:
        print("La calificación ingresada no es válida. Debe estar entre 0 y 100.")
except ValueError:
    print("Por favor, ingrese un número válido.")
