#Así debería funcionar la función
def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingresa un número: "))
    print(divisors(num))
    print("El programa finalizó")
#Esta función de acá funciona aunque no arroja error como tal, lo que hace es calcular mal

if __name__ == '__main__':
    run()