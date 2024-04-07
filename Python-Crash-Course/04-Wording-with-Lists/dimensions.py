# defining a tuple
print("====== defining a tuple ======")
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# we can't assign a new value to an item in a tuple
# dimensions[0] = 250

# looping through all values in a tuple
print("\n====== looping through all values in a tuple ======")
for dimension in dimensions:
    print(dimension)

# although we can't modify a tuple, you can assign a new value to a variable that holds a tuple
print("\n====== assign a new value to a variable that holds a tuple ======")
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

