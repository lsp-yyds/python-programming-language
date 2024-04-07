# modifying elements in a list
print("====== modifying elements in a list ======")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list
# appending elements to the end of a list
print("\n====== adding elements to a list ======")
print("====== appending elements to the end of a list ======")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
# inserting elements into a list
print("====== inserting elements into a list ======")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements from a list
print("\n====== removing elements from a list ======")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# removing on item using the pop() method
print("\n====== removing on item using the pop() method ======")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# popping items from any position in a list
print("\n====== popping items from any position in a list ======")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# removing an item by value
print("\n====== removing an item by value ======")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me.")
