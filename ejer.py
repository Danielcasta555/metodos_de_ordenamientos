#1. Ordenación de notas de estudiantes: Dado un arreglo de calificaciones, ordénalas de menor a
#mayor usando el método de burbuja.

def ordenacion_burbuja(calificaciones):
    n = len(calificaciones)
    for i in range(n):
        for j in range(0, n-i-1):
            if calificaciones[j] > calificaciones[j+1]:
               calificaciones[j], calificaciones[j+1] = calificaciones[j+1], calificaciones[j]
            return calificaciones
        
calificaciones = [85, 78, 92, 68, 88]
calificaciones_ordenadas = ordenacion_burbuja(calificaciones)
print("calificaciones ordenadas de menor a mayor ")
