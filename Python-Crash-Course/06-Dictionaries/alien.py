# a simple dictionary
print("====== a simple dictionary ======")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# accessing values in a dictionary
print("\n====== accessing values in a dictionary ======")
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(alien_0['points']) + " points!")

# adding new key-value pairs
print("\n====== adding new key-value pairs ======")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modifying values in a dictionary
print("\n====== modifying values in a dictionary ======")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# removing key-value pairs
print("\n====== removing key-value pairs ======")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
