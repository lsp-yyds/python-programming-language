import copy

# create lists with []
print("\n====== create lists with [] ======")
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]

# create or convert with list()
another_empty_list = list()
print(another_empty_list)
print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# create from a string with split()
print("\n====== create from a string with split() ======")
talk_like_a_pirate_day = '9/19/2019'
print(talk_like_a_pirate_day.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))
print(splitme.split('//'))

# get an item by [offset]
print("\n====== get an item by [offset] ======")
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

# get items with a slice
print("\n====== get items with a slice ======")
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])
marxes.reverse()
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])
print(marxes[-6:-4])

# add an item by offset with insert()
print("\n====== add an item by offset with insert() ======")
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo')
print(marxes)

# duplicate all items with *
print("\n====== duplicate all items with * ======")
print(["blah"] * 3)

# combine lists by using extend() or +
print("\n====== combine lists by using extend() or + ======")
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

# change an item by [offset]
print("\n====== change an item by [offset] ======")
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

# change items with a slice
numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers)
print(type(numbers[0]))
print(type(numbers[1]))

# delete an item by offset with del
print("\n====== delete an item by offset with del ======")
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
del marxes[-1]
print(marxes)
del marxes[1]
print(marxes)

# delete an item by value with remove()
print("\n====== delete an item by value with remove() ======")
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)

# get an item by offset and delete it with pop()
print("\n====== get an item by offset and delete it with pop() ======")
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)

# delete all items with clear()
print("\n====== delete all items with clear() ======")
work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)

# find an item's offset by value with index()
print("\n====== find an item's offset by value with index() ======")
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))

# test for a value with in
print("\n====== test for a value with in ======")
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)

words = ['a', 'deer', 'a', 'female', 'deer']
print('deer' in words)

# count occurrences of a value with count()
print("\n====== count occurrences of a value with count() ======")
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

# convert a list to a string with join()
print("\n====== convert a list to a string with join() ======")
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)

# reorder items with sort() or sorted()
print("\n====== reorder items with sort() or sorted() ======")
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)
marxes.sort()
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)

# get length with len()
print("\n====== get length with len() ======")
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))

# assign with =
print("\n====== assign with = ======")
a = [1, 2, 3]
print(a)
b = a
print(b)

a[0] = 'surprise'
print(a)
print(b)

b[0] = 'I hate surprise'
print(a)
print(b)

# copy with copy(), list(), or a slice
print("\n====== copy with copy(), list(), or a slice ======")
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)

# copy everything with deepcopy()
print("\n====== copy everything with deepcopy() ======")
a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(a)
print(b)
print(c)
print(d)

print("======")
a[2][1] = 10
print(a)
print(b)
print(c)
print(d)

print("======")
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)
a[2][1] = 10
print(a)
print(b)

# compare lists
print("\n====== compare lists ======")
a = [7, 2]
b = [7, 2, 9]
print(a == b)
print(a <= b)
print(a < b)

# iterate with for and in
print("\n====== iterate with for and in ======")
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)

# iterate multiple sequences with zip()
print("\n====== iterate multiple sequences with zip() ======")
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

print("======")
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))

# create a list with a comprehension
print("\n====== create a list with a comprehension ======")
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

number_list = list(range(1, 6))
print(number_list)

print("======")
number_list = [number for number in range(1, 6)]
print(number_list)
number_list = [number - 1 for number in range(1, 6)]
print(number_list)
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)

print("======")
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

cells = [(row, col) for row in range(1, 4) for col in range(1, 3)]

for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

# lists of lists
print("\n====== lists of lists ======")
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1][0])
