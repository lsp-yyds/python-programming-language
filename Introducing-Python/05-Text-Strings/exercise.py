import string
song = """When an ell grabs your arm,
And it causes great harm,
That's - a moray!"""

for line in song.split("\n"):
    for word in line.split(" "):
        if word.startswith("m"):
            song = song.replace(word, word.title())

print(song)