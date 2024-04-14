# create tuple with commas and ()
print("====== create tuple with commas and () ======")
empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

one_marx = ('Groucho',)
print(one_marx)

one_marx = ('Groucho')
print(one_marx)
print(type(one_marx))

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
print(type(marx_tuple))

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

one_marx = 'Groucho',
print(type(one_marx))
print(type('Groucho', ))
print(type(('Groucho',)))

# assign multiple variables at once
print("\n====== assign multiple variables at once ======")
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a)
print(b)
print(c)

# create with tuple()
print("\n====== create with tuple() ======")
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

# combine Tuples by using +
print("\n====== combine Tuples by using + ======")
print(('Groucho',) + ('Chico', 'Harpo'))

# duplicate items with *
print("\n====== duplicate items with * ======")
print(('yada',) * 3)

# compare tuples
print("\n====== compare tuples ======")
a = (7, 2)
b = (7, 2, 9)
print(a == b)
print(a <= b)
print(a < b)

# iterate with for and in
print("\n====== iterate with for and in ======")
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)

# modify a tuple
print("\n====== modify a tuple ======")
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
# tuples are immutable
# print(t1 + t2)
print(id(t1))
t1 += t2
print(t1)
print(id(t1))