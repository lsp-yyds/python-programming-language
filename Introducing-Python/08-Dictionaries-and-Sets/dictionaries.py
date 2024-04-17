import copy

# create with {}
print("\n====== create with {} ======")
empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)

# create with dict()
print("\n====== create with dict() ======")
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)
acme_customer = dict(first='Wile', middle='E', last='Coyote')
print(acme_customer)

# convert with dict()
print("\n====== convert with dict() ======")
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

los = ['ab', 'cd', 'ef']
print(dict(los))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

# add or change an item by [key]
print("\n====== add or change an item by [key] ======")
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}
print(some_pythons)

# get an item by [key] or with get()
print("\n====== get an item by [key] or with get() ======")
print(some_pythons['John'])
# print(some_pythons['Groucho'])
print('Groucho' in some_pythons)
print(some_pythons.get('John'))
print(some_pythons.get('Groucho', 'Not a Python'))
print(some_pythons.get('Groucho'))

# get all keys with keys()
print("\n====== get all keys with keys() ======")
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
}
print(signals.keys())
print(list(signals.keys()))

# get all values with values()
print("\n====== get all values with values() ======")
print(signals.values())
print(list(signals.values()))

# get all key-value pairs with items()
print("\n====== get all key-value pairs with items() ======")
print(signals.items())
print(list(signals.items()))

# get length with len()
print("\n====== get length with len() ======")
print(len(signals))

# combine dictionaries with {**a, **b}
print("\n====== combine dictionaries with {**a, **b} ======")
first = {
    'a': 'agony',
    'b': 'bliss'
}

second = {
    'b': 'bagels',
    'c': 'candy'
}

third = {
    'd': ['dress', 'drive']
}

print({**first, **second})

combine = {**first, **second, **third}
print(combine)
# shallow copy
third['d'][1] = 'desktop'
print(combine)

# combine dictionaries with update()
print("\n====== combine dictionaries with update() ======")
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}

others = {
    'Marx': 'Groucho',
    'Howard': 'Moe',
}

pythons.update(others)
print(pythons)

first = {
    'a': 1,
    'b': 2
}

second = {
    'b': 'platypus'
}

first.update(second)
print(first)

# delete an item by key with del
print("\n====== delete an item by key with del ======")
print(pythons)
del pythons['Howard']
print(pythons)
del pythons['Marx']
print(pythons)

# get an item key and delete it with pop()
print("\n====== get an item key and delete it with pop() ======")
print(pythons)
print(len(pythons))
print(pythons.pop('Palin'))
print(pythons)
print(len(pythons))
# pythons.pop('Palin')
print(pythons.pop('Palin', 'Hugo'))

# delete all items with clear()
print("\n====== delete all items with clear() ======")
pythons.clear()
# pythons = {}
print(pythons)

# test for a key with in
print("\n====== test for a key with in ======")
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Jones': 'Terry',
    'Palin': 'Michael',
    'Idle': 'Eric'
}

print('Chapman' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)

# assign with =
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

# copy with copy()
print("\n====== copy with copy() ======")
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera'
}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(original_signals)

# copy everything with deepcopy()
print("\n====== copy everything with deepcopy() ======")
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile']
}
signals_copy = signals
print(signals)
print(signals_copy)

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

print("======")

signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': ['stop', 'smile']
}
signals_copy = copy.deepcopy(signals)
print(signals)
print(signals_copy)

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

# compare dictionaries
print("\n====== compare dictionaries ======")
a = {
    1: 1,
    2: 2,
    3: 3
}

b = {
    3: 3,
    1: 1,
    2: 2
}

print(a == b)
# dictionaries only can be compared with
# the simple comparison operators == and !=
# print(a <= b)
a = {
    1: [1, 2],
    2: [1],
    3: [1]
}

b = {
    1: [1, 1],
    2: [1],
    3: [1]
}

print(a == b)

# iterate with for and in
print("\n====== iterate with for and in ======")
accusation = {
    'room': 'ballroom',
    'weapon': 'lead pipe',
    'person': 'Col. Mustard'
}

for key in accusation.keys():
    print(key)

print("======")

for value in accusation.values():
    print(value)

print("======")

for item in accusation.items():
    print(item)

print("======")

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

# dictionary comprehensions
print("\n====== dictionary comprehensions ======")
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)
