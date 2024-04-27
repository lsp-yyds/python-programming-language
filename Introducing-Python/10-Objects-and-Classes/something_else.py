from collections import namedtuple
from dataclasses import dataclass

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

print("======")
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)
print(duck2.bill)
print(duck2.tail)

print("======")
duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)
print(duck3.bill)
print(duck3.tail)


# dataclasses
# class TeenyClass:
#     def __init__(self, name):
#         self.name = name

@dataclass
class TeenyClass:
    name: str


print("\n====== dataclasses ======")
teeny = TeenyClass('itsy')
print(teeny.name)


@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0


snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
print(snowman)
print(duck)
print(snowman.teeth)
print(snowman.habitat)