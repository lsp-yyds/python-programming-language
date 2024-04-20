# define a function with def
print("====== define a function with def ======")


def do_nothing():
    pass


def make_a_sound():
    print('quack')


def agree():
    return True


def echo(anything):
    """echo returns its input argument"""
    return anything


def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


def print_args(*args):
    # if len(args) >= 1:
    # print('args[0]:', args[0])
    print('Positional tuple:', args)


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)


def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


def mangle(arg):
    arg[1] = 'terrible!'


def answer():
    print(42)


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something(func):
    func()


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


# call a function with parentheses
print("\n====== call a function with parentheses ======")
print(do_nothing())
print(make_a_sound())

if agree():
    print('Splendid!')
else:
    print('That was unexpected')

print(echo('Rumplestiltskin'))

comment = commentary('blue')
print(comment)

# none is useful
print("\n====== none is useful ======")

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

if thing is None:
    print("It's nothing")
else:
    print("It's something")

whatis(None)
whatis(True)
whatis(False)

# positional arguments
print("\n====== positional arguments ======")
print(menu('chardonnay', 'chicken', 'cake'))
print(menu('beef', 'bagel', 'bordeaux'))

# keyword arguments
print("\n====== keyword arguments ======")
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
print(menu('frontenac', dessert='flan', entree='fish'))

# specify default parameter values
print("\n====== specify default parameter values ======")
print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck', 'doughnut'))

buggy('a')
buggy('b')

# explode/gather positional arguments with *
print("\n====== explode/gather positional arguments with * ======")
args = (2, 5, 7, 'x')
print_args()
print_args(3, 2, 1, 'wait!', 'uh...')
print_args(args)
print_args(*args)
print("======")
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# explode/gather keyword arguments with **
print("\n====== explode/gather keyword arguments with ** ======")
print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# keyword-only arguments
print("\n====== keyword-only arguments ======")
data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print_data(data, start=4)
print_data(data, end=2)

# mutable and immutable arguments
print("\n====== mutable and immutable arguments ======")
outside = ['one', 'fine', 'day']
mangle(outside)
print(outside)

# docstrings
print("\n====== docstrings ======")
help(echo)
print("======")
print(echo.__doc__)

# function are first-class citizens
print("\n====== function are first-class citizens ======")
answer()
run_something(answer)
print("======")
print(type(answer))
print(type(run_something))
print("======")
run_something_with_args(add_args, 1, 2)
print(run_with_positional_args(sum_args, 1, 2, 3, 4))


# inner functions
def outer(a, b):
    def inner(c, d):
        return c + d

    return inner(a, b)


def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote

    return inner(saying)


print("\n====== inner functions ======")
print(outer(4, 7))
print(knights('Ni!'))


# closures
def knight2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying

    return inner2


print("\n====== closures ======")
a = knight2('Duck')
b = knight2('Hasenpfeffer')

print(a)
print(b)

print(a())
print(b())


# anonymous functions: lambda
def edit_story(words, func):
    for word in words:
        print(func(word))


def enliven(word):
    return word.capitalize() + '!'


print("\n====== anonymous functions: lambda ======")
stairs = ['thud', 'meow', 'thud', 'hiss']
edit_story(stairs, enliven)
print("======")
edit_story(stairs, lambda word: word.capitalize() + '!')


# generator functions
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


print("\n====== generator functions ======")
print(sum(range(1, 101)))
print(my_range)
ranger = my_range(1, 5)
print(ranger)
for x in ranger:
    print(x)
print("======")
for try_again in ranger:
    print(try_again)

# generator comprehensions
print("\n====== generator comprehensions ======")
genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))

print(genobj)
for thing in genobj:
    print(thing)


# decorator
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result

    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return new_function


# @document_it
# @square_it
@square_it
@document_it
def add_ints(a, b):
    return a + b


print("\n====== decorator ======")
cooler_add_ints = document_it(add_ints)
print(add_ints(3, 5))


# print("======")
# cooler_add_ints(3, 5)


# namespaces and scope
def print_global():
    print('inside print_global:', animal)
    # animal = 'wombat'
    # print('after the change:', animal)


# def change_and_print_global():
#     print('inside print_global:', animal)
#     animal = 'wombat'
#     print('after the change:', animal)


def change_local():
    animal = 'wombat'
    # print('inside change_local:', animal, id(animal))
    print('locals:', locals())


def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)


print("\n====== namespaces and scope ======")
animal = 'fruitbat'
print('at the top level:', animal)
print_global()
# change_and_print_global()
print(id(animal))
# change_local()
# change_and_print_global()
print("======")
print(animal)
change_local()
print('globals:', globals())


# uses of _ and __ in names
def amazing():
    """This is the amazing function.
    Want to see it again?"""
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)


print("\n====== uses of _ and __ in names ======")
amazing()


# recursion
def dive():
    return dive()


# def flatten(lol):
#     for item in lol:
#         if isinstance(item, list):
#             for subitem in flatten(item):
#                 yield subitem
#         else:
#             yield item

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


print("\n====== recursion ======")
# dive()
lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
print(flatten(lol))
print(list(flatten(lol)))

# async functions
print("\n====== async functions ======")

# exceptions
print("\n====== exceptions ======")
short_list = [1, 2, 3]
position = 5
# print(short_list[position])

# handle errors with try and except
print("\n====== handle errors with try and except ======")

try:
    print(short_list[position])
except IndexError:
    print('Need a position between 0 and', len(short_list) - 1, 'but got', position)

# while True:
#     value = input('Position [q to quit]? ')
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad index:', position)
#     except Exception as other:
#         print('Something else broke:', other)


# make your own exceptions
class UppercaseException(Exception):
    pass


print("\n====== make your own exceptions ======")
words = ['eenie', 'meenie', 'miny', 'MO']
try:
    for word in words:
        if word.isupper():
            raise UppercaseException(word)
except UppercaseException as err:
    print("UppercaseException:", err)

