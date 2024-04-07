# importing an entire module
# import pizza

# pizza.make_pizza(16, 'pepperoni')
# # pizza.make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')

# importing specific functions
# from pizza import make_pizza

# make_pizza(16, 'pepperoni')
# make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')

# using as to give a function an alias
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# using as to give a module alias
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')