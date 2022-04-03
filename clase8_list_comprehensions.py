#Vamos a imprimir una lista de los primeros 10 números naturales al cuadrado
def run():
    # squares = []
    # for i in range(1,11):
    #     if i % 3 !=0:
    #         squares.append(i**2)
    # print("imprimimos los primeros 10 números naturales al cuadrado")
    # print(squares)

    squares = [i**2 for i in range(1,11) if i % 3!=0]
    print(squares)
    #- para cada i en el rango que va de 1 hasta 11 voy a guardar esa i elevada al cuadrado solamente si la i modulo 3 es distinta de 0 
    #- en otras palabras: para cada i de los números del 1 a 11 voy a guardar esa i al cuadrado solamente si no es divisible por 3

if __name__ == '__main__':
    run()