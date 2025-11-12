'''class Person:
    name = ""
    age = 0

Prakash = Person()
Prakash.name = "Prakash"
Prakash.age = 21

print("Name:", Prakash)
print("Age:", Prakash.age)'''


class Person:
    def __init__(self, name, age):
        self.n=name
        self.a=age

Prakash = Person("Prakash",22)

print(Prakash.a)
print(Prakash.n)
print(Prakash)