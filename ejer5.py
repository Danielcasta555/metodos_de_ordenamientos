# Ordenación de precios de productos: Un sistema de inventario tiene precios desordenados. Ordénalos ascendentemente con burbuja.


def ordenacion_burbuja_precios(precios):
    n = len(precios)
    for i in range(n):
        for j in range(0, n-i-1):
            if precios[j] > precios[j+1]:
                precios[j], precios[j+1] = precios[j+1], precios[j]
    return precios

# Ejemplo de uso
precios = [20.5, 10.75, 30.0, 25.99, 15.5]
precios_ordenados = ordenacion_burbuja_precios(precios)
print("Precios ordenados ascendentemente:", precios_ordenados)
