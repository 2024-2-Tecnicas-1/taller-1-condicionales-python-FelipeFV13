def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    relacio_ab_c = not(c > (a+b))
    relacion_ac_b = not(b > (a+c))
    relacion_bc_a = not(a > (b+c))

    if relacio_ab_c and relacion_ac_b and relacion_bc_a:
        if(a== b and a==c):
            return "El triángulo es equilátero"
        elif a==b or a==c or b==c:
            return "El triángulo es isósceles"
        else:
            return "El triángulo es escaleno"
    else:
        return "No es un triángulo válido"


if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
