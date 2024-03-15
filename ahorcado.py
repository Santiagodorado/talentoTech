from random import choice

vida = 6
palabras = ['python', 'javascript', 'git', 'visual', 'datos', 'estructura', 'lista']
palabraSecreta = choice(palabras)
listPalabraSecreta = [i for i in palabraSecreta]
mostrar = ["-" for _ in palabraSecreta]

def esLetra(letra):
    return letra.isalpha()

def validarLetra(letra):
    if (letra in listPalabraSecreta):
        for i in range(len(listPalabraSecreta)):
            if (letra == listPalabraSecreta[i]):
                mostrar[i] = letra
            else:
                continue
    else:
        quitarVida()

def quitarVida():
    global vida
    vida -= 1

def mostrarVida():
    mostrarVida = "x" * vida
    print(f"\nSalud [ {mostrarVida} ]")

def imprimirPalabra():
    palabra = ' '.join(mostrar)
    print(f">> {palabra}")

def ganaste():
    return "-" not in mostrar

def perdiste():
    return vida == 0

def juego():
    print(f"Jugaremos ahorcado, adivina la palabra")
    while True:
        mostrarVida()
        imprimirPalabra()
        letra = input("Ingresa una letra: ").lower()
        while (not esLetra(letra)):
            letra = input("Debes ingresar una letra: ")
        validarLetra(letra)
        
        if (ganaste()):
            print("Adivinaste la palabra. Ganaste")
            break
        elif (perdiste()):
            print(f"La palabra era: {palabraSecreta}")
            break

juego()
