users = ['Ed', 'Ash', 'Jaan']

# print(users[1])
# print(users[1:2])
# print(users[1:])
# print(users[:2])

# Multiple values
alot_zeros = [0] * 20

# print(alot_zeros)

# unpacking
items = ['Laptop', 'Phone', ' Joystick']
laptop, phone, joystick = items
# print(phone)

laptop, *other = items
# print(other)

# Add Items
users.append('New Item')
users.insert(0, "Beginning Item")

print(users)

# Remove Items
users.pop()

print(users)


# Tupples
letters = ('a', 'b', 'b', 'c', 'd')

# Sets
letters = {'a', 'b', 'b', 'c', 'd'}
