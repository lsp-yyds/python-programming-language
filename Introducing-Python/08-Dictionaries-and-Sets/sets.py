# create with set()
print("\n====== create with set() ======")
empty_set = set()
print(empty_set)
even_number = {0, 2, 4, 6, 8}
odd_number = {1, 3, 5, 7, 9}
print(even_number)
print(odd_number)

# convert with set()
print("\n====== convert with set() ======")
print(set('letters'))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

# get length with len()
print("\n====== get length with len() ======")
reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))

# add an item with add()
print("\n====== add an item with add() ======")
s = set((1, 2, 3))
print(s)
s.add(4)
print(s)

# delete an item with remove()
print("\n====== delete an item with remove() ======")
s = set((1, 2, 3))
s.remove(3)
print(s)

# iterate with for and in
print("\n====== iterate with for and in ======")
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

# test for a value with in
print("\n====== test for a value with in ======")
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print("======")

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

# combinations and operators
print("\n====== combinations and operators ======")
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print("======")

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

print("======")

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

print(a & b)
print(a.intersection(b))
print(bruss & wruss)

print("======")

print(a | b)
print(a.union(b))
print(bruss | wruss)

print("======")

print(a - b)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)

print("======")

print(a ^ b)
print(a.symmetric_difference(b))

print("======")

print(a <= b)
print(a.issubset(b))
print(bruss <= wruss)
print(bruss.issubset(wruss))
print(a <= a)
print(a < b)
print(a < a)
print(bruss < wruss)

print("======")

print(a >= b)
print(a.issuperset(b))
print(wruss >= bruss)
print(a >= a)
print(a.issuperset(a))
print(a > b)
print(wruss > bruss)
print(a > a)

# set comprehensions
print("\n====== set comprehensions ======")
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

# create an immutable set with frozenset()
print("\n====== create an immutable set with frozenset() ======")
print(frozenset([3, 2, 1]))
print(frozenset([2, 1, 3]))
print(frozenset([3, 1, 2]))
print(frozenset([2, 3, 1]))

fs = frozenset([3, 2, 1])
print(fs)
# fs.add(4)