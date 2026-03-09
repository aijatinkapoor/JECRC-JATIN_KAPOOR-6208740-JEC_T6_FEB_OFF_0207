## function used in dictionery
'''
1.get
2.pop
3.popitem
4.update
5.Keys
6.Values
7.items'''

d={1:1,2:2,(1,2,3):(1,2,3)}
print(d)
print(d.get(2))
print(d.get('2'))
print(d[1])
print(d[(1,2,3)])

user={'username':'user123',
      'password':'******',
      'location':'IN'}
user1={'username':'user123',
      'password':'******',
      'location':'IN'}
user2={'username':'user123',
      'password':'******',
      'location':'IN'}
user.pop('location')
print(user)
user.pop('username','password')
print(user)

print(user1.popitem())
print(user1)

print(user2)
user2['password']='123'## update direct
print(user2)

user2.update({'password':'123456'})
print(user2)
user2.update({'password':'*******','is_logged_in':True})
print(user2)

print(user2.keys())
print(user2.values())
print(user2.items())