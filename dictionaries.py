user = {"name": "Ash", "email": "ash@ahoo.com",
        "age": 20, "purchases": [1, 2, 3, 4]}

user["name"] = 'ANNA'

# print(user["name"])
# print(user["email"])

# for key in user:
#     print(key)

# for key, val in user.items():
#     print(key)
#     print(val)

# print(user.items())

if "name" in user:
    print('It is!')

del user["purchases"]
print(user)
