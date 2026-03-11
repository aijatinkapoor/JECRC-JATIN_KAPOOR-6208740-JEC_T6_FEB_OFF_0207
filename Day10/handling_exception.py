import time
'''
n1, n2 = 20, 0

try:
    result = n1/n2
    print(result)
except ZeroDivisionError:
    print("please do not choose zero as n2")

print("Code after error")'''

'''try:
    a, b, c = 1, 2
except Exception:
    print("For performing MVC, n0. of variables must be equal")

try:
    print(a, b, c)
except:
    print("Identifiers are not there in memory")
'''


try:
    while True:
        print(time.time())
except KeyboardInterrupt:
    print("Loop got stopped!")