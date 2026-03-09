## function in using set
'''
1.add
2.remove
3.discard
4.pop
5.clear
6.union
7.intersection
8.difference
9.symmetric_difference'''

set1={1,3,4,56,7,3,2,1}
print(set1)
set1.add(50)
print(set1)
set1.add(50)
print(set1)

s2={'a','c','A',7,9,4,7,2,True,False,(3+9j)}
print(s2)
s2.remove('a')
print(s2)
s2.discard('c')
s2.discard(10)
print(s2)
s2.pop()
s2.pop()
print(s2)

u1={1,2,3,4}
u2={3,2,67,33,'a'}
print(u1.union(u2))
print(u1.intersection(u2))
print(u1.difference(u2))##uncommon elment return from first set+

print(u1.symmetric_difference(u2))