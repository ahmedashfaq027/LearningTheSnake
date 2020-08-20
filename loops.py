# For loop
users = ["Ed", "Anna", "John", "Podrick", "Smith"]

# for user in users:
# print('Hello there user')
# print(user)

# for i in range(0, 20):
#     print('I RUN 20 times')

my_list = list(range(0, 101, 5))
print(my_list)

name = list('Edwin')
# print(name)


# While loop
age = 10
while age < 20:
    age += 1
    if(age == 14):
        print("I am independant now")
        # break
        continue
    print(age)
