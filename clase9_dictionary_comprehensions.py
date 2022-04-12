"""
Vamos a crear un diccionario, cuyas llaves sean los primeros 10 números naturales y los valores estén elevados al cubo
"""
def run():
    my_dict = {}
    #guardar en cada una de las i que van a ser las llaves de nuestro diccionario elevada al cubo
    for i in range(1,11):
        my_dict[i] = i**3
    print(my_dict)
    print("***números impares***")
    my_dict2 ={}
    for i in range(1,11):
        if i % 3 != 0:
            my_dict2[i] = i**3
    print(my_dict2)
    """
    dict comprehensions
    """
    print("números impares con dict comprehension")
    """
    - para cada i en el rango de 1 a 11 voy a guardar a i como llave e i elevado al cubo como valor, solamente si i modulo 3 es distinto de 0
    - en otras palabras:
        para cada número de 1 a 11 voy a guardar ese número como llave y ese número elevado al cubo como valor si ese número no es divisible entre 3
    """
    num = {i: i**3 for i in range (1,11) if i % 3 != 0}
    print(num)

if __name__ == '__main__':
    run()