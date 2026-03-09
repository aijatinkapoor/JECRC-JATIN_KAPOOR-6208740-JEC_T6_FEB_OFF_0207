# Function inbuilt
'''
1.lower
2.upper
3.Capitalize
4.tittle
5.strip
6.lstrip
7.rstrip
8.replace
9.index
10.split
11.join
12.startswith
13.endswith
14.isdigit
15.isalpha
16.islower
17.isupper'''

s1='Pyt  v hOn1234&@#$%^(&*)'
s='JECRC'
st='My name is Harsh'
print(s.lower())## return value
print(s.upper())
# print(help(str.capitalize))## ussed to know information about particular
print(s.capitalize)
# print(help(str.title))
print(s.title())
print(s.strip('C'))
print(s.rstrip())
print('   Python'.lstrip())
print(s.replace('JECRC','RTU'))
print(s.replace('J','R'))
# print(help(str.index))
print(st.index("Harsh"))
print(st.find('Harsh'))
print(st.find('harsh'))
# print(help(str.split))
print(st.split())
print(st.split('is'))
st2='I-LOVE-PYTHON-PROGRAMMING-LANGUAGE'
print(st2.split('-'))
list_of_str=st2.split('-')
print('@'.join(list_of_str))

# print(help(str.startswith))
print(st2.startswith('I'))
print(st2.endswith('LANGUAGE'))
print(s1.isalpha())
print(s1.isdigit())
print(s1.islower())
print(s1.isupper())