# checking for inequality
print("====== checking for inequality ======")
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# numerical comparisons
print("\n====== numerical comparisons ======")
answer = 42

if answer < 0 or answer > 100:
    print("invalid number!")
elif answer != 42:
    print("That is not the correct answer. Please try again!")
    if answer < 42:
        print("Too Small!")
    elif answer > 42:
        print("Too Big!")
else:
    print("lucky!")

# checking whether a value is in a list
print("\n====== checking whether a value is in a list ======")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' not in requested_toppings)

# checking that a list is not empty
requested_toppings = []
print("\n====== checking that a list is not empty ======")
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# using multiple lists
print("\n====== using multiple lists ======")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("Finish making your pizza!")
