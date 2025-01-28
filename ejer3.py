#3. Temperaturas diarias: Un sensor registra las temperaturas de una semana. Ordena los valores

def ordenacion_burbuja_temperaturas(temperaturas):
    n = len(temperaturas)
    for i in range(n):
        for j in range(0, n-i-1):
            if temperaturas[j] > temperaturas[j+1]:
                temperaturas[j], temperaturas[j+1] = temperaturas[j+1], temperaturas[i]
        return temperaturas

temperaturas = [22.5, 18.3, 20.0, 25.1, 19.8, 21.0, 23.5]  
temperaturas_ordenadas = ordenacion_burbuja_temperaturas(temperaturas)
print("temperaturas ordenadas de menor a mayor", temperaturas_ordenadas)          