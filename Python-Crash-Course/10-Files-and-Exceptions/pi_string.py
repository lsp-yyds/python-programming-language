# reading line by line
print("====== reading line by line ======")

file_path = ('/home/bruce/Projects/PycharmProjects/python-programming-language/Python-Crash-Course/10-Files-and'
             '-Exceptions/text_files/pi_digits.txt')

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))