# reading from a file
print("====== reading from a file ======")

file_path = ('/home/bruce/Projects/PycharmProjects/python-programming-language/Python-Crash-Course/10-Files-and'
             '-Exceptions/text_files/pi_digits.txt')

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())