#4. Orden de llegada de corredores: Dado un listado de tiempos de llegada en una carrera, ordénalos de menor a mayor usando burbuja.

def ordenacion_burbuja_tiempos(tiempos):
    n = len(tiempos)
    for i in range(n):
        for j in range(0, n-i-1):
            if tiempos[j] > tiempos[j+1]:
                tiempos[j], tiempos[j+1] = tiempos[j+1], tiempos[j]
    return tiempos

# Ejemplo de uso
tiempos = [12.5, 15.3, 10.0, 14.1, 11.8, 13.0, 16.5]
tiempos_ordenados = ordenacion_burbuja_tiempos(tiempos)
print("Tiempos de llegada ordenados de menor a mayor:", tiempos_ordenados)
