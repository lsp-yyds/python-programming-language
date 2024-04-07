# changing case in a string with methods
name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.lower())
print(name.upper())

# combining or concatenating strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# stripping whitespace
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())