def shell_sort(arr):
    n = len(arr)
    # Inicia con el gap más grande y lo reduce a la mitad en cada iteración
    gap = n // 2

    while gap > 0:
        # Ordenamiento por inserción modificado para elementos separados por el gap
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Mover elementos del subgrupo hacia sus posiciones correctas
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Colocar el elemento actual en su posición
            arr[j] = temp
            print(arr)

        # Reducir el gap
        gap //= 2

# Ejemplo de uso
arr = [9, 8, 3, 7, 5, 6, 4, 1]
shell_sort(arr)
print("Array ordenado:", arr)
