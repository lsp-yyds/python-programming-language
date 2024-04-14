import string

print('snap')
print("Crackle")

print("'Nay!' said the naysayer, 'Neigh?' said the horse.")
print('The rate double quote in captivity: ".')
print('A "two by four" is actually 1 1/2" x 3 1/2".')
print("'There's the man that shot my paw!' cried the limping hound.")

print('''Boom!''')
print("""Eek!""")

print("\n====== multiline strings ======")
poem = '''There was a Young Lady of Norway.
    Who casually sat in a doorway;
    When the door squeezed her flat,
    She exclaimed, "What of that?"
    This courageous Young Lady of Norway.'''

print(poem)

poem = '''There was a Young Lady of Norway. \
Who casually sat in a doorway; \
When the door squeezed her flat, \
She exclaimed, "What of that?" \
This courageous Young Lady of Norway.'''

print()
print(poem)

# empty string
print("\n====== empty string ======")
print('')
print("")
print('''''')
print("""""")

# create with str()
print("\n====== create with str() ======")
print(str(98.6))
print(str(1.0e4))
print(str(True))

# combine by using +
print("\n====== combine by using + ======")
print('Release the kraken! ' + 'No, wait!')
vowels = ('a'
          "e" '''i'''
          'o' """u""")
print(vowels)

# duplicate with *
print("\n====== duplicate with * ======")
start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

# get a character with []
print("\n====== get a character with [] ======")
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])
print(letters[5])

# get a substring with a slice
print("\n====== get a substring with a slice ======")
print(letters[:])
print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
# from the start to the end, in steps of 7 characters
print(letters[::7])
# from offset 4 to 19, by 3
print(letters[4:20:3])
# from offset 19 to the end, by 4
print(letters[19::4])
# from the start to offset 20 by 5
print(letters[:21:5])
print(letters[-1::-1])
print(letters[::-1])

# get length with len()
print("\n====== get length with len() ======")
print(len(letters))

# split with split()
print("\n====== split with split() ======")
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split())
print(tasks.split(','))

# combine by using join()
print("\n====== combine by using join() ======")
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print(crypto_string)

# substitute by using replace()
print("\n====== substitute by using replace() ======")
setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
print(setup.replace('a ', 'a famous ', 100))

# strip with strip()
print("\n====== strip with strip() ======")
world = "   earth   "
print(world.strip())
print(world.lstrip())
print(world.rstrip())

blurt = "What the...!!?"
print(blurt.strip('.?!'))
print(string.whitespace)    # '\t\n\r\x0b\x0c'
print(string.punctuation)
print(blurt.strip(string.punctuation))

prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))

# search and select
print("\n====== search and select ======")
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))

print("======")
word = 'the'
print(poem.find(word))
print(poem.index(word))
print(poem.rfind(word))
print(poem.rindex(word))
print(poem.count(word))

print("======")
word = 'duck'
print(poem.find(word))
print(poem.rfind(word))
# print(poem.index(word))
# print(poem.rindex(word))

print("======")
# Are all of the characters in the poem either letters or numbers?
print(poem.isalnum())
print(poem.isalpha())

# case
print("\n====== case ======")
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())

# alignment
print("\n====== alignment ======")
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))

# formatting
print("\n====== formatting ======")
# old style: %
print("====== old style: % ======")
# an integer
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

# a float
print("======")
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

# an integer and a literal %
print("======")
print('%d%%' % 100)

# string and integer interpolation
print("======")
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

# some examples for a string
print("======")
thing = 'woodchuck'
print('%s' % thing)
print('%12s' % thing)
print('%+12s' % thing)
print('%-12s' % thing)
print('%.3s' % thing)
print('%12.3s' % thing)
print('%-12.3s' % thing)

# a float with %f variants
print("======")
thing = 98.6
print('%f' % thing)
print('%12f' % thing)
print('%+12f' % thing)
print('%-12f' % thing)
print('%.3f' % thing)
print('%12.3f' % thing)
print('%-12.3f' % thing)

# an integer with %d
print("======")
thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)

# new style: {} and format()
print("\n====== new style: {} and format() ======")
thing = 'woodchuck'
place = 'lake'
d = {
    'thing': 'duck',
    'place': 'bathtub'
}
print('{}'.format(thing))
print('The {} is in the {}.'.format(thing, place))
print('The {1} is in the {0}.'.format(place, thing))
print('The {thing} is in the {place}'.format(thing='duck', place='bathtub'))
print('The {0[thing]} is in the {0[place]}'.format(d))

print("======")
thing = 'wraith'
place = 'window'
print('The {} is at the {}'.format(thing, place))
print('The {:10s} is at the {:10s}'.format(thing, place))
print('The {:<10s} is at the {:<10s}'.format(thing, place))
print('The {:^10s} is at the {:^10s}'.format(thing, place))
print('The {:>10s} is at the {:>10s}'.format(thing, place))
print('The {:!^10s} is at the {:!^10s}'.format(thing, place))

# newest style: f-strings
print("\n====== newest style: f-strings ======")
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
print(f'The {thing:>20} is in the {place:.^20}')
print(f'{thing = }, {place = }')
print(f'{thing[-4:] = }, {place.title() = }')
print(f'{thing = :>4.4}')