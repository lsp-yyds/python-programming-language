"""
python's basic data types

Name            Type        Mutable?    Examples
Boolean         bool        no          True, False
Integer         int         no          47, 25000, 25_000
Floating point  float       no          3.14, 2.7e5
Complex         complex     no          3j, 5 + 9j
Text string     str         no          'alas', "alack", '''a verse attack'''
List            list        yes         ['Winken', 'Blinken', 'Nod']
Tuple           tuple       no          (2, 4, 8)
Bytes           bytes       no          b'ab\xff'
ByteArray       bytearry    yes         bytearry(...)
Set             set         yes         set([3, 5, 7])
Frozen set      frozenset   no          frozenset(['Elsa', 'Otto'])
Dictionary      dictionary  yes         {'game': 'bingo', 'dog': 'dingo', 'drummer': 'Ringo'}
"""

print(type(True))
print(type(25_000))
print(type(2.7e5))
print(type(3j))
print(type('alas'))
print(type(['Winken', 'Blinken', 'Nod']))
print(type((2, 4, 8)))
print(type(b'ab\xff'))
print(type(bytearray(b'ab\x00')))
print(type({3, 5, 7}))
print(type(frozenset(['Elsa', 'Otto'])))
print(type({'game': 'bingo', 'dog': 'dingo', 'drummer': 'Ringo'}))

print(isinstance(7, int))