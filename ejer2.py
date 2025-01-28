#2. Ordenación de nombres por longitud: Ordena una lista de nombres según la cantidad de
#caracteres utilizando ordenamiento burbuja.

def ordenacion_burbuja_longitud(nombres):
    n = len(nombres)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(nombres[j]) > len(nombres[j+1]):
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
    return nombres

nombres = ["Ana", "Alejandro", "Juana", "Daniel", "Carlos", "David"]
nombres_ordenados = ordenacion_burbuja_longitud(nombres)
print("Nombres ordenados por longitud:", nombres_ordenados) 