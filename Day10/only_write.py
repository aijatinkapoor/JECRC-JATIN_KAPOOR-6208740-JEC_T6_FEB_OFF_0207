file = open('temp.txt', 'w')

file.write('I am the first line')

file.writelines([
    'first line\n',
    'second line\n',
    'third line\n',
    'forth line\n',
    'fifth line\n',
])
file.close()