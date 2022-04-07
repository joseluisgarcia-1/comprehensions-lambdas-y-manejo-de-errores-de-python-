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