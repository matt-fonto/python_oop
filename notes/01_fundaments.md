# Fundaments Python Syntax

- Arrays are called lists
- Objects are called dictionaries

## Variable and data types

- variable: bucket that stores some data
- Python uses snake case, not camel case
  - python_variable | jsVariable

```py
x = 10 # int
y = 3.14 # float
name = 'Matt' # str => we can use single or double quotes
is_active = True  # bool

a, b, c = 1, 2, 3 # multiple assignment
```

## Arithmetic operations

- `**`: exponent operator. We raise a number to the power of another number
- `//`: floor division. Gives us the integer result of the division. not the float. Removes the decimal points, and gives us the base int.
- `%`: modulus. Gives us the remainder of the division
- BEDMAS: Represents the order of operations. Brackets, exponents, division, multiplication, addition, subtraction

```py
result = base ** exponent

print(2**3) # 2 * 2 * 2 => 8
print(5**4) # 5 * 5 * 5 * 5 => 625
```

## Input vs Output

```py
print(variable | result) # output

user_name = input('Name: ') # returns a string

def say_hello(name:str):
    return f"Hello, {name}"

print(say_hello(user_name))

num = input('number: ')
print(int(num) + 10) # if we don't convert to int or float, it will throw error
```

## String methods

- `.method()`

```py
hello_upper = 'hello'.upper()
hello_lower = 'hello'.lower()

# Important string methods
.upper()
.lower()
.capitalize()
.count('ll') # returns the ocorrences of a substring
```

## Conditional operators

- They return `bool`
- We can write expressions on both sides of the conditional operators, which will be resolved first, then compared

```py
==  #equality
!=  #inequality
> # greater than
>= # greater than or equal to
< # less than
<= # less than or equal to
```

### Chained conditions

- Terminology: operands or expressions
- Operands: values or expressions being evaluated by the logical operators
- Expressions: more general term, which can be simple values (True, False) or more complex evaluations (x > 5)

```py
x and y # `x` and `y` are operands

# both operands/expressions need to be true
and # right and left side expressions need to be true

# only one needs to be true
or # either right or left side need to true

# neither can be true
not # neither right nor left side can be true
```

## Control flow

- Refers to the order in which individual instructions, statements, or blocks of code are executed or evaluated.
- It determines how a program's logic flows based on conditions, loops, and branching
- Types of control flow:
  - 1. sequential execution: code run line by line, top to bottom
  - 2. conditional statement (branching): program takes decision based on conditions
  - 3. loops (iteration): repeat block of code until a condition is met or no longer valid
  - 4. function calls: jumping to and returning from reusable blocks of code

### If-else statements

```py
x = 10

if x > 5:
    print ("x is greater than five")
elif x == 5:
    print ("x is equal to five")
else:
    print ("x is less than five")
```

- Python doesn't have a switch statement as JS, C and Java

### For loops

- Iterate over a range or any iterable (list, tuples, dictionaries)

```py
# Basic range loop
for i in range(5):
    print(i)

# Loop list
numbers = [1, 2, 3, 4, 5]
# for item in iterable:
# directly iterates over the elements, not the index
# each number refers to an element in the list
# useful when we need only the value
for number in numbers:
    print(number)

# for i in range(len(iterable))
# go through the indeces [0, 1, 2, 3, ...]
# access each elements via its index numbers[i]
# useful when we need both the value and the index
for i in range(len(numbers)):
    print(numbers[i])

# other way to achieve this is to use enumberate
# for i, value in enumarate(iterable)
for i, element in enumerate(numbers):
    print(i, element)

# Inverted loop list: we just use the `reversed` function
for number in reversed(numbers):
    print(number)

# Inverted loop with range => range(start, stop, step)
for i in range(10, 0, -1):  # similar to js (for let i = 10; i > 0, i--)
    print(i)


# Loop dictionary
person = {name:"Mateus", age: 28, profession: "Software Engineer"}
for key, value in person.items():
    print(f"{key}: {value}")

# Loop array of dictionaries (list of dictionaries)
people = [
    {"name": "Alice", "age": 30, "profession": "Teacher"},
    {"name": "Bob", "age": 25, "profession": "Doctor"},
    {"name": "Charlie", "age": 35, "profession": "Driver"}
]
for person in people:
    print(f"{person['name']} is {person['age']} years old and is a {person['profession'].lower()}")
```

### While loop

```py
while condition == True:
    do something

count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions

```py
# function with default parameter
def greet(name="World"):
    return f"Hello, {name}!"

print(greet("Mateus")) # Hello, Mateus!
print(greet()) # Hello, World!

def func(x,y):
    return x + y, x - y, x * y, x / y # returns a tuple

sum_result, sub_result, mult_result, div_result = func(10, 20) # unpacking the tuple
```

### Unpack operators - `*args` and `**kwargs`

## Lists

- Python's arrays are dynamic and called **lists**

```py
numbers = [1,2,3]
numbers.append(4) # add element
numbers.remove(2) # remove element by value
print(numbers)

# List comprehesion
squared = [x**2 for x in range(5)]
print(squared) # [0, 1, 4, 9, 16]
```

- The values inside the list are stored by reference, so we can change them

```py
x = [1, 'hey', False]
x[0] = 'jelly'
print(x)
```

## Tuples

- Immutable sequences

```py
point = (1,2)
print(point[0]) # 1

x, y = point
```

## Dictionaries

- Key-value pairs, similar to objects in JS
- Differently from JS, where we can access object properties with dot notation, in Python we need to use bracket notation
- In Py, dot notation ised used to access attributes for objects, not dictionary keys. Meaning, if `person` were a class instance (object) with an attribute `name`, we'd be able to use dot notation.
- Dot notation: only for class instances, not normal objects

```py
person = {"name":"Matt", "age":28}
print(person["name"]) # in python, we can't access dictionary properties with dot notation `person.name`, as we would in JS

# In Python, dictionaries require the use of bracket notation `person["age"]`
```

## Sets

- Unordered collections of unique elements

```py
# list -> []
# tuple -> ()
# set -> {}

unique_numbers = {1,2,3,3}
print(unique_numbers)
```

## Classes

- Used in OOP

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

person_1 = Person("Matt", 28)
print(person.greet())
```

## File handling

```py
# Write to file
with open("example.txt", "w") as file:
    file.write("Hello, world")

# Read from file
with open("example.txt". "r") as file:
    content = file.read()
    print(content)
```

## Error handling

- `try-except` for exception handling

```py
try:
    # code
except:
    # certain condition
finally:
    # always runs

try:
    result = 10/0
except ZeroDivisionError as e:
    print(f"Error {e}")
finally:
    print("This will always execute")
```

## Importing modiules

- Use built-in or third-party libraries

```py
import math
print(math.sqrt(16)) # 4.0

from math import pow, pi
print(pow(2,3)) # 8.0
print(pi)
```

## List comprehension

- Concise way to create or transform a list by applying an expression to each element in an iterable (list, dictionary, set, range, string)

```py
# return [expression]
# for item in iterable
# only when [condition] is met
[expression for item in iterable if condition]
```

- expression: operation to be applied to each element
- item: each element from the iterable
- iterable: the source data
- condition (optional): a filter to include only elements satisfying the condition

```py
numbers = [1,2,3,4,5,6]

squared = [num**2 for num in numbers]
evens = [num for num in numbers if num % 2 == 0] # [2, 4, 6]
doubled_evens = [num**2 for num in numbers if num % 2 == 0] # [4, 8, 16]
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]
```

## List vs. Tuple

- Both data structures store collection of items

| feature           | tuple      | list                       |
| ----------------- | ---------- | -------------------------- |
| definition        | ()         | []                         |
| mutability        | immutable  | mutable                    |
| performance       | faster     | slower                     |
| use case          | fixed data | dynamic or modifiable data |
| methods available | limited    | more extensive             |

## Iterables in Python

- Iterable: object that can return its elements one at a time
- list, tuple, set, dict, str

```py
from collections.abc import Iterable

print(isinstance([1,2,3], Iterable)) # True: list
print(isinstance((1,2,3), Iterable)) # True: tuple
print(isinstance(123, Iterable)) # False: int
```
