#Para trabajar con reduce tengo que importarla
from functools import reduce
print("con list comprehension antes de filter")
my_list = [1,4,5,6,9,13,19,21]
odd = [i for i in my_list if i %2 != 0]
print(odd)
print("con filter")
nm = list(filter(lambda x:x %2 !=0, my_list ))
print(nm)
print("con list comprehensions antes de función map")
my_list2 = [1,2,3,4,5]
squares = [i**2 for i in my_list2]
print(squares)
print("con map")
square = list(map(lambda x:x**2, my_list2))
print(square)
print("Con for antes de la función reduce")
my_list_three = [2,2,2,2,2]
all_multiplied = 1

for i in my_list_three:
    all_multiplied = all_multiplied * i
print(all_multiplied)
print("con la función reduce")
all_multiplied_reduce = reduce(lambda a,b:a*b, my_list_three)
print(all_multiplied_reduce)