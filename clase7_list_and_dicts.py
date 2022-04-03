def run():
    my_list = [1,2,3, "hola", False, 4.5]
    my_dict = {'messi': 'psg', 'haaland': 'borussia'}

    super_list = [
        {'mbappe': 'psg', 'nationality': 'francia'},
        {'ronaldo': 'united', 'nationality': 'portugal'},
        {'ibra': 'milan', 'nationality': 'suecia'},
        {'varane': 'united', 'nationality': 'francia'},
        {'kanté': 'chelsea', 'nationality': 'francia'}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,-3,-4,-5],
        "floating_nums": [5.4, 5.6, 7.6]
    }

    for key, value in super_dict.items():
        print("imprimos las listas del diccionario:",key, "=",value)

if __name__ == '__main__':
    run()