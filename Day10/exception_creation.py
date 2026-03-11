'''num = 16

if num>= 18:
    print("you are eligible for voting")

else:
    raise NameError("Age should be less than or equals to 18!")'''

'''lass RaiseError(Exception):
    pass

num = 16

if num>= 18:
    print("you are eligible for voting")

else:
    raise RaiseError("Age should be less than or equals to 18!")'''

s = input()

assert s == s[::-1], print("It is not a palindromic String!")
print("It is a palindromic string!")