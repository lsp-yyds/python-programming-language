# return values
print("====== return values ======")


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = str(first_name) + ' ' + str(last_name)
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# making an argument optional
print("\n====== making an argument optional ======")


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = str(first_name) + ' ' + str(middle_name) + ' ' + str(last_name)
    else:
        full_name = str(first_name) + ' ' + str(last_name)
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

