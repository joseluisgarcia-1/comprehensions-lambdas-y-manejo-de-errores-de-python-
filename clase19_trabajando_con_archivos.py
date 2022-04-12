#con esta función lo que hacemos es crear un archivo en la carpeta numbers con el nombre de names.txt y usamos el metodo w
# en ese documento colocamos los nombres que están en la lista names, y si por ejemplo al momento de escribir un nombre lo escribí mal
#y quiero escribirlo como es realmente lo que hago es corregir y el programa me sobre escribe ese dato, valga la redundancia lo actualiza
def write():
    #colocamos el encoding para el manejo de caracteres especiales como tildes
    names = ["Messi", "Ronaldo", "Mbappe", "Haaland"]
    with open("./numbers/names.txt", "w", encoding="utf-8") as nombres:
        for name in names:
            nombres.write(name)
            nombres.write("\n")
#con esta función si por ejemplo tenemos ya un archivo en este caso el archivos names.txt y lo que queremos es agregarle información sin que
#el archivo original sobre escriba lo que ya está entonces usamos la denominación "a" que significa append(agregar)
def overwrite():
    names = ["Psg", "Man United", "Psg", "Dourtmund"]
    with open("./numbers/names.txt", "a", encoding="utf-8") as nombres:
        for name in names:
            nombres.write(name)
            nombres.write("\n")

def read():
    numbers = []
    #colocamos el encoding para el manejo de caracteres especiales como tildes
    with open("./numbers/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def run():
    write()
    read()
    overwrite()

if __name__ == '__main__':
    run()
    