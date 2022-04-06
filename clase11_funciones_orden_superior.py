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