### Object-Oriented Programming (OOP)

1. What is OOP?

- OOP (Object-Oriented Programming) is a programming paradigm based on objects and classes.
- It helps write organized, reusable, and scalable code.


2. Key Concepts of OOP

There are 4 pillars of OOP:

1️⃣ Encapsulation
2️⃣ Inheritance
3️⃣ Polymorphism
4️⃣ Abstraction


3. Class and Object

# Class
A blueprint/template for creating objects.

# Object
An instance of a class with data + behavior.

```Example:
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

mycar = Car("BMW", 2022)
```


4. Encapsulation

- Wrapping data + methods together in a class.

- It also allows data hiding.

```Example
class Student:
    def __init__(self):
        self.name = "John"
        self._age = 20       # protected
        self.__marks = 90    # private
```




5. Inheritance

One class (child) can acquire properties of another class (parent).

Types:

- Single inheritance
- Multiple inheritance
- Multilevel inheritance
- Hierarchical inheritance
- Hybrid inheritance

```Example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):   # Inherits Animal
    pass

d = Dog()
d.speak()
```

6. Polymorphism

"One name, many forms"

Types:

- Compile-time (not in Python)
- Run-time (method overriding)


```Example (Overriding):
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")
```


```Example (Same function, different behavior):
print(len("Hello"))
print(len([1,2,3]))
```


7. Abstraction

Hiding complex details, showing only essential features.



```Example using abc module:
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")
```



8. Constructor & Destructor


# Constructor
Initializes object — __init__() method.

# Destructor
Called when object is destroyed — __del__() method.


```Example:
class Test:
    def __init__(self):
        print("Object Created")
    
    def __del__(self):
        print("Object Destroyed")
```



9. Method Types in OOP


1. Instance Method

Works with object data.

```
def fun(self):
    pass
```


2. Class Method

Works with class, not objects.


```
@classmethod
def fun(cls):
    pass
```


3. Static Method

Independent function inside class.

```
@staticmethod
def fun():
    pass
```



10. Object Class

All Python classes inherit from the base object class.




11. Method Overloading & Overriding


# Overloading

Same method name, different arguments
(Python does NOT support true overloading)

```
# Python workaround
def add(a=None, b=None, c=None):
    return (a or 0) + (b or 0) + (c or 0)
```


# Overriding

Child class replaces parent method.


```
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
```



12. Super()

Used to call parent class methods.


```
class A:
    def show(self):
        print("A method")

class B(A):
    def show(self):
        super().show()
        print("B method")
```


13. Multiple Inheritance

```
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```


14. MRO (Method Resolution Order)

Determines order of class searching in multiple inheritance.

View MRO:

```
C.mro()
```


15. Composition vs Inheritance


#  Inheritance → “is-a relationship”

Example: Dog is a Animal

# Composition → “has-a relationship”

Example: Car has a Engine





