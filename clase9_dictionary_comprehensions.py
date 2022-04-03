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
    for i in range(1,101):
        if i % 3 != 0:
            my_dict2[i] = i**3
    print(my_dict2)

if __name__ == '__main__':
    run()