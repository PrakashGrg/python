'''
def sum():
    a=55
    b=45
    return a+b
sum()


def sum(a,b):
    add =a+b
    print(add)
sum(45,55)


def sum():
    a=10
    b=20
    add=a+b
    print(add)
sum()


def add(a, b):
    return a + b
print(add(15, 3))

def subtract(a, b):
    return a - b
print(subtract(53, 3))


def divide(a, b):
    if b == 0:
        return "not"
    return a / b
print(divide(100, 10))


def modulus(a, b):
    return a % b
print(modulus(1000, 10))


keys = ["name", "age", "city"]
values = ["Jester", 22, "Pokara"]

for key, value in dict.items():
    print(key, value)


age = input("Enter your age: ")
print ("the age is ",age )


age = input("Enter your age: ")
name = input("Enter your name: ")
address = input("Enter your address: ")
print ("The age is ",age, "The name is", name, "The address is", address)



age_str = input("Enter your age: ")
age = int(age_str)

if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")
else:
    print("You are not an adult")
    print("You cannot vote")
    print("You do not have full legal rights")



a="15"
c = int(a)
e = float(a)

print("type",type(a))
print("type",type(c))
print("type",type(e))


'''