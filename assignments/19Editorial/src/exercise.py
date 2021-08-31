import math
def main():
    # escribe tu código abajo de esta línea
    num_palabras = int(input("Dame el número de palabras: "))
    calculo = math.ceil(num_palabras/475)*(60)*(0.90)
    print("El costo de la publicación es: ", calculo)


if __name__ == '__main__':
    main()