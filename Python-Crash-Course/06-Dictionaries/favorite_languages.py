# a dicitonary of similar objects
print("====== a dicitonary of similar objects ======")
favorite_languages = {
    'jen': 'c++',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print(favorite_languages)

friends = []
languages = []

for name in favorite_languages.keys():
    friends.append(name)

print("My friends:", friends)

for language in favorite_languages.values():
    languages.append(language)

print("Languages:", languages)

print("\n====== looping through a dictionary ======")
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

for name in sorted(favorite_languages.keys()):
    print(name)