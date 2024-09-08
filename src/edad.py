from time import localtime


def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    t = localtime()
    day = t.tm_mday
    month = t.tm_mon
    year = t.tm_year

    edad = (year - anno)-1

    if mes == month and day >= dia:
        edad += 1
        return f"Usted tiene {edad} años"
    elif mes < month:
        edad += 1
        return f"Usted tiene {edad} años"
    else:
        return f"Usted tiene {edad} años"

    return "";

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
