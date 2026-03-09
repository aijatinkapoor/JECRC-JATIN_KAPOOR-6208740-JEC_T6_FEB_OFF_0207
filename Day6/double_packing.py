'''
def func_name(**kwargs):
    Statement
    Block'''

#func_name(k1=va1,k2=val2,....,kn=valn)
# all the key names should a string but you cant use quotes

def print_details(**kwargs):
    print(kwargs)
print_details(username='user123',password='****',logged_in_devices=['Android','Window','Linux'])