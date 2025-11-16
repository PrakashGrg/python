# Report

## Prepared By
**Name:** Prakash Gurung
**Program:** Python, Django
**Date:** November 2025


---

## 1. Introduction

Python is a powerful and easy-to-learn programming language created by Guido van Rossum in 1991.
It is widely used for web development, software development, data analysis, mathematics, and automation.

## It is used for:

1. web development (server-side),
2. software development,
3. mathematics,
4. system scripting.

## What can Python do?

1. Python can be used on a server to create web applications.
2. Python can be used alongside software to create workflows.
3. Python can connect to database systems. It can also read and modify files.
4. Python can be used to handle big data and perform complex mathematics.
5. Python can be used for rapid prototyping, or for production-ready software development.

## Why Python?

1. Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
2. Python has a simple syntax similar to the English language.
3. Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
4. Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
5. Python can be treated in a procedural way, an object-oriented way or a functional way.

## Good to know

1. The most recent major version of Python is Python 3, which we shall be using in this tutorial.
2. In this tutorial Python will be written in a text editor. It  is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

## Python Syntax compared to other programming languages

1. Python was designed for readability, and has some similarities to the English language with influence from mathematics.
2. Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
3. Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.



## Example
print("Hello, World!")



# Python Statements

## Statements

-> A computer program is a list of "instructions" to be "executed" by a computer.
-> In a programming language, these programming instructions are called statements.

## Example
print("Python is fun!")

## Many Statements

-> Most Python programs contain many statements.

-> The statements are executed one by one, in the same order as they are written:

## Example
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")


-> The first statement is executed first (print "Hello World!").
-> Then the second statement is executed (print "Have a good day.").
-> And at last, the third statement is executed (print "Learning Python is fun!").


# Python Variables

## Variables

-> Variables are containers for storing data values.

## Creating Variables

-> Python has no command for declaring a variable.
-> A variable is created the moment you first assign a value to it.

## Example
x = 5
y = "John"
print(x)
print(y)

-> Variables do not need to be declared with any particular type, and can even change type after they have been set.

## Example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

## Casting

-> If you want to specify the data type of a variable, this can be done with casting.

##Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

## Get the Type
-> You can get the data type of a variable with the type() function.

## Example
x = 5
y = "John"
print(type(x))
print(type(y))


## Single or Double Quotes?

->String variables can be declared either by using single or double quotes:

## Example
x = "John" # is the same as
x = 'John'

## Case-Sensitive
-> Variable names are case-sensitive.

## Example
-> This will create two variables:

a = 4
A = "Sally"
#A will not overwrite a


# Python - Variable Names

## Variable Names
-> A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

-> Rules for Python variables:

1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)
5. A variable name cannot be any of the Python keywords.

## Example
Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Python Data Types

## Built-in Data Types
-> In programming, data type is an important concept.

-> Variables can store data of different types, and different types can do different things.

-> Python has the following data types built-in by default, in these categories:

1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
8. None Type:	NoneType


## Getting the Data Type

-> You can get the data type of any object by using the type() function:

## Example
-> Print the data type of the variable x:
x = 5
print(type(x))


## Setting the Data Type

-> In Python, the data type is set when you assign a value to a variable:

Example	Data Type
x = "Hello World"	str
x = 20	int
x = 20.5	float
x = 1j	complex
x = ["apple", "banana", "cherry"]	list
x = ("apple", "banana", "cherry")	tuple
x = range(6)	range
x = {"name" : "John", "age" : 36}	dict
x = {"apple", "banana", "cherry"}	set
x = frozenset({"apple", "banana", "cherry"})	frozenset
x = True	bool
x = b"Hello"	bytes
x = bytearray(5)	bytearray
x = memoryview(bytes(5))	memoryview
x = None	NoneType



## Setting the Specific Data Type

-> If you want to specify the data type, you can use the following constructor functions:

Example	Data Type
x = str("Hello World")	str
x = int(20)	int
x = float(20.5)	float
x = complex(1j)	complex
x = list(("apple", "banana", "cherry"))	list
x = tuple(("apple", "banana", "cherry"))	tuple
x = range(6)	range
x = dict(name="John", age=36)	dict
x = set(("apple", "banana", "cherry"))	set
x = frozenset(("apple", "banana", "cherry"))	frozenset
x = bool(5)	bool
x = bytes(5)	bytes
x = bytearray(5)	bytearray
x = memoryview(bytes(5))	memoryview


## Python Numbers
-> There are three numeric types in Python:

1. int
2. float
3. complex
-> Variables of numeric types are created when you assign a value to them:

## Example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

-> To verify the type of any object in Python, use the type() function:

## Example
print(type(x))
print(type(y))
print(type(z))

## Int
-> Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

## Example
```Integers:

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))```


## Float
-> Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

## Example
```Floats:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))```

-> Float can also be scientific numbers with an "e" to indicate the power of 10.

## Example
```Floats:

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))```


## Complex

-> Complex numbers are written with a "j" as the imaginary part:

## Example
```Complex:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))```


## Type Conversion
-> You can convert from one type to another with the int(), float(), and complex() methods:

## Example
```Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))```
-> Note: You cannot convert complex numbers into another number type.

## Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

## Example
```Import the random module, and display a random number from 1 to 9:```

import random
print(random.randrange(1, 10))```