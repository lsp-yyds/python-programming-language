# writing to a file
print("====== writing to a file ======")

filename = 'programming.txt'

# overwrite
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")

# appending to a file
with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")