# Sorting a list permanently with the sort() method
print("====== Sorting a list permanently with the sort() method ======")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with the sorted() method
print("\n====== sorting a list temporarily with the sorted() method ======")
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars)

# printing a list in reverse order
print("\n====== printing a list in reverse order ======")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)