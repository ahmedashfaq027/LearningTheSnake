def greeting():
    print('Hello there my friend')
    print('What is your name')
    name = input()
    print("nice to meet you "+name)

# greeting()


def greetName(name):
    print("hello there ed" + name)


greetName('10')


def mulBy10(number):
    return 10*number


mul_num = mulBy10(20)
print(mul_num)


def add(number, by=1):
    return number+by


added_num = add(10)
added_num = add(10, 30)
added_num = add(number=10, by=20)
print(added_num)
