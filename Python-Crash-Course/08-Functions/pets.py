# keyword arguments and default values
print("====== keyword arguments and default values ======")
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + str(pet_name).title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(pet_name='willie')