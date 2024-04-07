# defining a function
print("====== defining a function ======")


def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()

# passing information to a function
print("\n====== passing information to a function ======")


def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + str(username).title() + "!")


greet_user('jesse')