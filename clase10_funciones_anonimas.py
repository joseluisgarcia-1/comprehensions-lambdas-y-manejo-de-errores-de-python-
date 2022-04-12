palindrome = lambda string:string == string[::-1]
print(palindrome('oso'))

"""
con una función normal, esa función lambda quedaría así:
"""
# def palindrome(string):
#     return string == string[::-1]
# print(palindrome('ana'))