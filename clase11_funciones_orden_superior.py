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
print("list comprehension normal")
my_list = [1,4,5,6,9,13,19,21]
answer_one = [i for i in my_list if i % 2 !=0]
print(answer_one)
print("function filter con function lambda")
answer_two = list(filter(lambda x: x%2!=0, my_list))
print(answer_two)
my_list_two = [1,2,3,4,5]
print()
print("function list comprehension normal")
my_list_three = [1,2,3,4,5]
squares = [i**2 for i in my_list_three]
print(squares)
print("function map con function lambda")
answer_three = list(map(lambda x:x**2,my_list_three))
print(answer_three)
print()

print("function de como hacerlo también en lugar de reduce")
my_list_four = [2,2,2,2,2]
all_multiplied = 1

for i in my_list_four:
    all_multiplied = all_multiplied * i
print(all_multiplied)

print("function reduce")
from functools import reduce

my_list_five = [2,2,2,2,2]
all_multi = reduce(lambda a,b: a*b, my_list_five)
print(all_multi)
