# define a class with class
class Cat:
    pass


print("\n====== define a class with class ======")
a_cat = Cat()
print(a_cat)
another_cat = Cat()
print(another_cat)

# attributes
print("\n====== attributes ======")
a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.namesis = another_cat

print(a_cat.age)
print(a_cat.name)
print(a_cat.namesis)
# print(a_cat.namesis.name)

a_cat.namesis.name = "Mr. Bigglesworth"
print(a_cat.namesis.name)


# methods
class Cat:
    def __init__(self, name):
        self.name = name


print("\n====== methods ======")
furball = Cat('Grumpy')
print("Our latest addition: ", furball.name)


# inheritance
class Car:
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    # pass
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")


print("\n====== inheritance ======")
print(issubclass(Yugo, Car))
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


# override a method
class Person:
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


print("\n====== override a method ======")
person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

# add a method
print("\n====== add a method ======")
give_me_a_yugo.need_a_push()


# get help from your parent with super()
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


print("\n====== get help from your parent with super() ======")
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)


# multiple inheritance
class Animal:
    def says(self):
        return 'I speak!'


class Horse(Animal):
    def says(self):
        return 'Neigh!'


class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


print("\n====== multiple inheritance ======")
print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())


# mixins
class PrettyMixin:
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


print("\n====== mixins ======")
t = Thing()
t.name = "Myarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()

# in self defense
print("\n====== in self defense ======")
a_car = Car()
a_car.exclaim()

Car.exclaim(a_car)


# attribute access
# getters and setters
class Duck:
    def __init__(self, input_name):
        # self.name = input_name
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


print("\n====== attribute access ======")
print("====== getters and setters ======")
fowl = Duck('Daffy')
# print(fowl.name)
don = Duck('Donald')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())


# properties for computed values
class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


print("\n====== properties for computed values ======")
c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.radius)
print(c.diameter)


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


print("\n====== name mangling for privacy ======")
fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
# print(fowl.__name)
print("======")
print(fowl._Duck__name)


# class and object attributes
class Fruit:
    color = 'red'


print("\n====== class and object attributes ======")
blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)
blueberry.color = 'blue'
print(blueberry.color)
print("======")
Fruit.color = 'orange'
print(Fruit.color)
print(blueberry.color)