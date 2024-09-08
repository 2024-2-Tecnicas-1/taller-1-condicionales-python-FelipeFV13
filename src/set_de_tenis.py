def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    if num_victorias_a >= 5 and num_victorias_b >= 5:
        if num_victorias_a <= 7 and num_victorias_b <= 7:
            if num_victorias_a == num_victorias_b:
                return "Aún no termina"
            elif num_victorias_a == 7:
                return "Ganó A"
            elif num_victorias_b == 7:
                return "Ganó B"
            else:
                return "Aún no termina"

        else:
            return "Inválido"
    else:
        if num_victorias_a <= 6 and num_victorias_b <= 6:
            if num_victorias_a == 6 and (num_victorias_a - num_victorias_b) >= 2:
                return "Ganó A"
            elif num_victorias_b == 6 and (num_victorias_b - num_victorias_a) >= 2:
                return "Ganó B"
            else:
                return "Aún no termina"
        else:
            return "Inválido"

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
