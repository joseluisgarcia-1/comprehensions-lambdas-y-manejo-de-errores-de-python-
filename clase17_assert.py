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
    num = input("Ingresa un número: ")
    #.isnumeric() -> lo que hace es devolver verdadero si ese string corresponde a una especie de número
    #y si por el contrario es ingresa una letra se activa el mensaje
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("El programa finalizó")
if __name__ == '__main__':
    run()