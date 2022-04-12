def divisors(num):
    try:
        if num < 0:
            raise ValueError("Ingrese un número positivo")
        else:
            divisors = [i for i in range(1,num+1) if num % i == 0]
            return divisors
    except ValueError as ve:
        print(ve)
        return str(num) + " No es un número positivo"

def run():
    #A esta función lo que vamos a decirle es que nos capture que si le pasamos una letra nos diga: que no podemos ingresar una letra
    #que estamos esperando que ingrese es un número, eso lo hacemos con el try, except
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("El programa finalizó")
    except ValueError as ve:
        print("Debes ingresar un número")
        #print(ve)
if __name__ == '__main__':
    run()