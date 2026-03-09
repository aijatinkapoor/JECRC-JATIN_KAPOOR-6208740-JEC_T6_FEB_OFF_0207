##Create a function which can take n no. of inputs from the user and return the sum of only int or floating point numbers Please make sure that user is capable of passing all type of values.
def sum_nums(*args):
    print(args,type(args))
    total = 0
    for i in args:
            if type(i) in (int,float):
                total += i
            else:
                 continue    
    print(f'Sum of numeric values: {total}')
    

sum_nums(1, 2.5, "hello", 3, [1, 2], 4.5, True, None, 10)