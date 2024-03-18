from random import choice

def palabraAzar():
    palabras = ['python', 'javascript', 'git', 'visual', 'datos', 'estructura', 'lista']
    palabraSecreta = choice(palabras)
    return palabraSecreta

def mostrarGuiones(palabra):
    mostrar = ["-" for _ in palabra]
    print(''.join(mostrar))

def quitarVida(vida):
    vida -= 1
    return vida

def esLetra(letra):
    return letra.isalpha()

def estaLetra(letra, palabra):
    return letra in palabra

def aciertos(letra, palabra, aciertos):
    for i in range(len(palabra)):
            if (letra == palabra[i]):
                aciertos[i] = letra
    return aciertos
 
def main():
    vida = 6
    palabra = palabraAzar()
    palabraOculta = ['-' for _ in palabra]
    letrasIncorrectas = []
    print("Jugaremos ahorcado, adivina la palabra oculta: ")
    print(f">> {' '.join(palabraOculta)}")
    while True:
        letra = input("Ingresa una letra: ")
        while not esLetra(letra) or letra in letrasIncorrectas or len(letra) > 1:
            letra = input("Debes ingresar una letra válida: ")

        if (estaLetra(letra, palabra)):
            correcta = ' '.join(aciertos(letra, palabra, palabraOculta))
            if (palabra == correcta.replace(" ", "")):
                print(f">> {correcta}")
                print("\nGanaste. Adivinaste la palabra")
                break
        else:
            letrasIncorrectas.append(letra)
            vida = quitarVida(vida)
            if(vida == 0):
              print(f"\nPerdiste. La palabra era {palabra}") 
              break 
        
        if (len(letrasIncorrectas) > 0):
            print(f"\nVida [ {"x" * vida} ]\nLetras incorrectas: {', '.join(letrasIncorrectas)}")
        else:
            print(f"\nVida [ {"x" * vida} ] ")
        print(f">> {correcta}")

if __name__ == "__main__":
    main()
