# Dada lista desordenada de números enteros. Tu tarea es escribir una función que reciba
# esta lista y devuelva una nueva lista con los elementos ordenados en orden ascendente.
# Implementa la función utilizando un algoritmo de ordenamiento propio (no se permite el
# uso de funciones nativas como sort(), sorted(), Arrays.sort(), etc.).
# La función debe devolver una nueva lista, no modificar la original.
# Definición de la función
# integerSort(inputArray: Array):
# Array Casos de ejemplo
# ● Con inpútArray = [5, -2, 10, 0, 3, -7],
# la salida debería ser integerSort (inputArray) = [-7, -2, 0, 3, 5, 10]

def integerSort(inputArray):
    original = inputArray[:]
    sorted_list = []

    while original:
        smallest = original[0]
        for num in original:
            if num < smallest:
                smallest = num
        original.remove(smallest)
        sorted_list.append(smallest)

    return sorted_list

