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

