# Looping through an entire list
print("====== Looping through an entire list ======")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# doing more work within a for loop
print("\n====== doing more work within a for loop ======")
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")