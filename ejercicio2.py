def letrasOrden(palabra):
    letras = []
    for i in palabra:
        if i not in letras:
            letras.append(i)

    letrasOrdenadas = sorted(letras)
    print(letrasOrdenadas)

letrasOrden('ejercicios')