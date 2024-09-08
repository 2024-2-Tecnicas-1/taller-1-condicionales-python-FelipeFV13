def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    valor = ord(caracter)

    if 48 <= valor <= 57:
        return "Es número"
    elif 65 <= valor <= 90:
        return "Es letra mayúscula"
    elif 97 <= valor <= 122:
        return "Es letra minúscula"
    else:
        return "No es letra ni número"




if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
