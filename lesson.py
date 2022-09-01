print("hello")
print("say \"I don't know\"")

print('hello, \nHow are you?')
print(r'C:\name\name')

print("""\
line1
line2
line3
line4\
""")

print('Hi' * 3 + 'Mike')
print('Py''thon')
prefix = 'Py'
print(prefix + 'thon')

s = ('aaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbb')

print(s)

word = 'python'
print(word[0])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
print('#######################')
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)
print('########################')

s = 'My name is Mike'
print(s)
is_start = s.startswith('My')
print(is_start)

print('####################')
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

print('##################')
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))
if 100 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_sprit = s.split(' ')
print(to_sprit)
x = '########'.join(to_sprit)
print(x)

print('##########################')

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
# y = x.copy()
y = x[:]
print('y =', y)
print('x =', x)
X = 20
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)

print('#########################')
