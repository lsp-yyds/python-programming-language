# passing an arbitrary number of arguments


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")

    for topping in toppings:
        # Print the list of toppings that have been requested.
        print("- " + topping)
