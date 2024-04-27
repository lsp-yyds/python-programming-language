# attribute access
print("====== attribute access ======")


# direct access
# class Duck:
#     def __init__(self, input_name):
#         self.name = input_name
#
#
# print("====== direct access ======")
# fowl = Duck('Daffy')
# print(fowl.name)
#
# fowl.name = 'Daphne'
# print(fowl.name)


# getters and setters
# class Duck:
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#
#
# print("====== getters and setters ======")
# don = Duck('Donald')
# print(don.get_name())
# don.set_name('Donna')
# print(don.get_name())


# properties for attribute access
# class Duck:
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#
#     name = property(get_name, set_name)
#
#
# print("====== properties for attribute access ======")
# don = Duck('Donald')
# print(don.get_name())
# don.set_name('Donna')
# print(don.get_name())
#
# don.name = 'Donald'
# print(don.get_name())


# class Duck:
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.hidden_name
#
#     @name.setter
#     def name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#
#
# print("====== properties for attribute access ======")
# fowl = Duck('Howard')
# print(fowl.name)
# fowl.name = 'Donald'
# print(fowl.name)


# properties for computed values
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


print("====== properties for computed values ======")
c = Circle(5)
print(c.radius)
print(c.diameter)
# c.diameter = 10


# name mangling for privacy
class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


print("====== name mangling for privacy ======")
fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)


# class and object attributes
class Fruit:
    color = 'red'


print("====== class and object attributes ======")
blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)

blueberry.color = 'blue'
print(blueberry.color)
print(Fruit.color)

Fruit.color = 'orange'
print(Fruit.color)

new_fruit = Fruit()
print(new_fruit.color)


# method types
# instance methods
# when you see an initial self argument in methods within a class definition, it's an instance method

# class methods
class A:
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects")


print("====== class methods ======")
easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()


# static methods
class CoyoteWeapon:
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


print("====== static methods ======")
CoyoteWeapon.commercial()


# magic methods
class Word:
    def __init__(self, text):
        self.text = text

    def equals(self, other):
        return self.text.lower() == other.text.lower()

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("' + self.text + '")'


print("====== magic methods ======")
first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first.equals(second))
print(first.equals(third))
print(first == second)
print(first == third)
print(first)


# aggregation and composition
class Bill:
    def __init__(self, description):
        self.description = description


class Tail:
    def __init__(self, length):
        self.length = length


class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')


print("\n====== aggregation and composition ======")
a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()