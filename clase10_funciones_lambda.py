from tkinter.messagebox import RETRY


palindrome = lambda string:string == string [::-1]
print("¿oso es palíndrome?:",palindrome('oso'))
print("¿carro es palíndrome?:",palindrome('carro'))
print("Con una función normal")
def palindro(palabra):
    return palabra == palabra[::-1]
print("¿oro es palíndrome?:",palindro('oro'))
print("¿casa es palíndrome?:",palindro('coro'))