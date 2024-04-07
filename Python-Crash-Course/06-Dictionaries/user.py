# looping through all key-value pairs
print("\n====== looping through all key-value pairs ======")
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key in user_0.keys():
    print(key)

for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value)