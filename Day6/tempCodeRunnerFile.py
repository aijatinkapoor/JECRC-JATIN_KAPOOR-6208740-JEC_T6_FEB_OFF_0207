def add_nums(*arg):
    # arg=list(arg)
    print(arg,type(arg))
    sum=0
    for i in arg:
        sum+=i
    print(f'Addition:{sum}')

add_nums(1,2,3,4,5,1.9,98.2,1)