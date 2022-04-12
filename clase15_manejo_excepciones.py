#Aquí le estamos pasando un entero y nos da error
# def palindromo(string):
#     return string == string[::-1]
# print(palindromo(1))

#Aquí le estamos pasando un string y nos arroja True o False de acuerdo a la palabra que le estemos pasando
def palindromo(string):
    return string == string[::-1]
print(palindromo("ana"))
print()
print("Función con la excepción, try, except")
def palindrome(palabra):
    return palabra == palabra[::-1]
try:
    print(palindrome("hola"))
except TypeError:
    print("Solo se puede ingresar letras")

print("Función con la excepción, try, except pero con una cadena vacía")
def palindrome(palabra):
    return palabra == palabra[::-1]
try:
    print(palindrome(""))
except TypeError:
    print("Solo se puede ingresar letras")
print()
print("Función con la excepción, raise y como ejemplo una cadena vacía")
def palind(letras):
    try:
        if len(letras) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return letras == letras[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palind(""))
except TypeError:
    print("Solo se pueden ingresar letras")

try:
    f = open("apuntes.txt")
finally:
    f.close()