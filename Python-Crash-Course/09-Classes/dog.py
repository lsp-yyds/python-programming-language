class Dog:
    """
    A simple attempt to model a dog.

    - public members

    Public members (generally methods declared in a class) are accessible from outside the class.
    The object of the same class is required to invoke a public method. This arrangement of private instance variables
    and public methods ensures the principle of data encapsulation.

    name = 'willie'

    - protected members

    Protected members of a class are accessible from within the class and are also available to its sub-classes.
    No other environment is permitted access to it.
    This enables specific resources of the parent class to be inherited by the child class

    _name = 'willie'

    - private members

    Python doesn't have any mechanism that effectively restricts access to any instance variable or method.
    Python prescribes a convention of prefixing the name of the variable/method with a single or double underscore to
        emulate the behavior of protected and private access specifiers.

    __name = 'willie'
    """

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title(), " rolled over!")


my_dog = Dog('willie', 6)

# accessing attributes
print("====== accessing attributes ======")
print(my_dog.name)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# calling methods
print("\n====== calling methods ======")
my_dog.sit()
my_dog.roll_over()

# creating multiple instances
print("\n====== creating multiple instances ======")
your_dog = Dog('lucy', 3)
print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()