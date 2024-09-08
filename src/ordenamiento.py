def evaluar(numero1, numero2, numero3, numero4):
    # TODO: Coloca aquí el código del ejercicio 5: Ordenamiento
    arr = [numero1, numero2, numero3, numero4]
    mensaje = ""

    for i in range(0, len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        auxiliar = arr[i]
        arr[i] = arr[min]
        arr[min] = auxiliar

    for i in range(0, len(arr)):
        mensaje += f"{arr[i]} "
    return mensaje.strip()


if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
