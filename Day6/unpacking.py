'''
add_int_float(*eval(input('Enter a list of values:)))'''

def sum_nums(*args):
    print(args,type(args))
    total = 0
    for i in args:
            if type(i) in (int,float):
                total += i
            else:
                 continue    
    print(f'Sum of numeric values: {total}')
    
sum_nums(*eval(input('Enter a list of values: ')))